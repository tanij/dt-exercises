FROM duckietown/challenge-aido_lf-template-random:daffy-amd64

RUN pip3 install -U "pip>=20.2"
COPY requirements.* ./
RUN cat requirements.* > .requirements.txt
RUN  pip3 install --use-feature=2020-resolver -r .requirements.txt

RUN mkdir /code/solution
COPY launchers /code
COPY solution /code/solution

CMD ["bash", "/code/run_agent.sh"]
