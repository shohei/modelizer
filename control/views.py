# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
import serial
from control.models import Camfile
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    port = serialOpen
    if(port == ""):
        port = "No PORT"
    if request.POST:
        mil = request.POST['milData']
        drl = request.POST['drlData']
        dim = request.POST['dimData']
        newCam = Camfile(milData=mil,drlData=drl,dimData=dim)
        newCam.save()
        return render_to_response('control/index.html',{'port':port,'mil':mil,'drl':drl,'dim':dim},context_instance=RequestContext(request))
    else:
        return render_to_response('control/index.html',{'port':port},context_instance=RequestContext(request))


def serialOpen():
    com = serial.Serial(port="/dev/tty.Bluetooth-Incoming-Port",baudrate=9600,bytesize=8,parity='N',stopbits=1,timeout=None,xonxoff=0,rtscts=True,writeTimeout=None,dsrdtr=True)
    return com.portstr

def hellotest(request):
    return HttpResponse("hello world")

def milUpload(request):
    if request.POST:
        milData = request.POST['milData']
    else:
        print("HOGE request")
        milData = "no data available"
    return render_to_response('control/index.html',{'milData':"no data available"},context_instance=RequestContext(request))


def drlUpload(request):
    if request.method == 'POST':
        drldata = request.POST['drill']

    else:
        drldata = "no data available"
    return HttpResponse("hello drilling world")

def dimUpload(request):
    if request.POST:
        dimdata = request.POST['dim']
    else:
        dimdata = "no data available"
    return HttpResponse("hello dimension world")


def startMilling(request):
    if request.POST:
        milData = request.POST['milData']
        print(milData)
        driveModela(milData)
    return render_to_response('control/index.html',{},context_instance=RequestContext(request))


def driveModela(rmlData):
    com = serial.Serial(port=2,baudrate=9600,bytesize=8,parity='N',stopbits=1,timeout=None,xonxoff=0,rtscts=True,writeTimeout=None,dsrdtr=True)
    print(com.portstr)
    com.write(rmlData)
    com.close()

def up(request):
    #print "up"
    #return HttpResponse("Hello, UP!")
    #port = "COM4"
    port = "UP! Driver"
    return render_to_response('control/up.html',{'port':port},context_instance=RequestContext(request))

def laser(request):
    print "laser"
    return HttpResponse("Hello, Laser!")
