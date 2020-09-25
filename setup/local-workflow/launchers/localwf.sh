#!/bin/bash

source /environment.sh

# initialize launch file
dt-launchfile-init

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------


# NOTE: Use the variable DT_REPO_PATH to know the absolute path to your code
# NOTE: Use `dt-exec COMMAND` to run the main process (blocking process)

function log_pid() {
  echo "[$BASHPID] $1"
}

function start_car_interface() {
  log_pid "Starting car interface..."
  #./launch_car_interface.sh
  #./catkin_ws/src/dt-car-interface/launch.sh &>/dev/null &
  /launch/dt-car-interface/default.sh &
  if [ $? -ne 0 ]; then
    log_pid "error while starting car interface"
    exit 1
  fi
  log_pid "Car interface started"
}

function start_notebook() {
  log_pid "Starting notebook in second thread"
  jupyter-notebook --allow-root --ip="*" --no-browser &
  if [ $? -ne 0 ]; then
    log_pid "Received error while running jupyter notebook"
    exit 1
  fi
  log_pid "Done running notebook" 
}

# launching app
set -e # now catch errors and stop
jupyter nbextension enable --py --sys-prefix jupyros
start_car_interface
start_notebook
log_pid "Starting solution.py"
dt-exec python3 $DT_REPO_PATH/packages/ros-bridge/solution.py


# ----------------------------------------------------------------------------
# YOUR CODE ABOVE THIS LINE

# wait for app to end
dt-launchfile-join
