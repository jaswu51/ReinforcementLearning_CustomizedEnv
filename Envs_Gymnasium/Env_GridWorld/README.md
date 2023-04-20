# build yor own env

* setup.py to specify the versions and packages requirements

* under the same name folder, gymexamples, register your env

* envs/ folder, to build your own enviroments GridWorldEnv, including the reset, step, render and close functions

* wrappers/ folder, to wrap your spaces accordingly. and it it not neccesary

* compile your env using !python3 -m pip install -e gymexamples

* test your env using !python3 test.py