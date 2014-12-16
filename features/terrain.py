#import lettuce
import subprocess
import multiprocessing
import pqaut.client
from lettuce import *


@before.all
def before_all():
    print 'running before all'
    #lettuce.world.application = multiprocessing.Process(target=app.run)
    world.application = subprocess.Popen(['python','/Users/matt/workspace/instruments/foo.py'])
    pqaut.client.wait_for_automation_server()


@after.all
def after_all(*args, **kwargs):
    subprocess.Popen.kill(world.application)
