#!/usr/bin/env python3

import io

import numpy as np
from PIL import Image

from aido_schemas import (
    Context,
    DB20Commands,
    DB20Observations,
    EpisodeStart,
    JPGImage,
    LEDSCommands,
    logger,
    protocol_agent_DB20,
    PWMCommands,
    RGB,
    wrap_direct,
    GetCommands,
)


class RandomAgent:
    n: int

    def init(self, context: Context):
        self.n = 0
        context.info("init()")
        self._rgb = None
        self.l_max = 0.1
        self.r_max = 0.1
        self.left = None
        self.right = None


    def on_received_seed(self, data: int):
        np.random.seed(data)

    def on_received_episode_start(self, context: Context, data: EpisodeStart):
        context.info(f'Starting episode "{data.episode_name}".')

    def on_received_observations(self, context: Context, data: DB20Observations):
        logger.info("received", data=data)
        camera: JPGImage = data.camera
        odometry = data.odometry
        # print(odometry)
        _rgb = jpg2rgb(camera.jpg_data)
        self._rgb = _rgb


    def on_received_get_commands(self, context: Context, data: GetCommands):
        gain = 0.1
        if self._rgb is None:
            pwm_left = 0.0
            pwm_right = 0.0
        else:
            gray0 = np.mean(self._rgb, axis=2).astype(np.float32)
            if self.left is None:
                self.gray0 = gray0

                left = np.zeros(gray0.shape, dtype=np.float32)
                right = np.zeros(gray0.shape, dtype=np.float32)
                h, w = gray0.shape[0:2]
                half = int(w/2)
                hh = int(h/3)
                left[:hh, 0:half] = 1 
                right[:hh, half:] = 1
                self.left = left
                self.right = right

            context.info(f'image module: {np.sum(gray0)}')
            context.info(f'left module: {np.sum(self.left)}')


            # gray = gray0 - self.gray0
            gray = gray0
            l = np.sum(gray * self.left)
            r = np.sum(gray * self.right)
            context.info(f'l: {l} r: {r}')
            self.l_max = max(l, self.l_max)
            self.r_max = max(r, self.r_max)
            ls = l / self.l_max
            rs = r / self.r_max
            context.info(f'ls: {ls} rs: {rs}')


            pwm_left= rs * gain
            pwm_right = ls * gain

        context.info(f'pwm: {pwm_left:.1f} rs: {pwm_right:.1f}')

        col = RGB(0.0, 0.0, 1.0)
        col_left = RGB(pwm_left,pwm_left,0.0)
        col_right = RGB(pwm_right, pwm_right, 0.0)
        led_commands = LEDSCommands(col, col_left, col_right, col_left, col_right )
        pwm_commands = PWMCommands(motor_left=pwm_left, motor_right=pwm_right)
        commands = DB20Commands(pwm_commands, led_commands)
        context.write("commands", commands)

    def finish(self, context: Context):
        context.info("finish()")


def jpg2rgb(image_data: bytes) -> np.ndarray:
    """ Reads JPG bytes as RGB"""

    im = Image.open(io.BytesIO(image_data))
    im = im.convert("RGB")
    data = np.array(im)
    assert data.ndim == 3
    assert data.dtype == np.uint8
    return data


def main():
    node = RandomAgent()
    protocol = protocol_agent_DB20
    wrap_direct(node=node, protocol=protocol)


if __name__ == "__main__":
    main()
