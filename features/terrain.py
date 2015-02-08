import lettuce
import subprocess
import multiprocessing
import pqaut.client
from lettuce import *
import bjsonrpc
import time

@before.all
def before_all():
    pass
    #lettuce.world.application = multiprocessing.Process(target=app.run)
    world.application = subprocess.Popen(['python','/Users/matt/workspace/instruments/app.py'])
    pqaut.client.wait_for_automation_server()
    lettuce.world.qtapp = bjsonrpc.connect(host='0.0.0.0', port=9001)

@after.all
def after_all(*args, **kwargs):
    subprocess.Popen.kill(world.application)


@before.each_step
def before_each_step(step):
    time.sleep(1)

