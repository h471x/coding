#declaring a class Light switch
class LightSwitch():
  #here the default instance variable
  def __init__(self):
    self.on = False
  #here are the methods
  def turnOn(self):
    self.on = True

  def turnOff(self):
    self.on = False

  def show(self):
    print(f"Light is {'on' if self.on else 'off'}")

  def nature(self):
    print(type(self))

#defining a dimmer class
class dimmer():
  def __init__(self):
    self.on = False
    self.bright = 0  #here to declare we will be using all along the methods

  def turnOn(self):
    self.on = True

  def turnOff(self):
    self.on = False

  def dimUp(self):
    if self.bright < 10:
      self.bright = self.bright + 1

  def dimDown(self):
    if self.bright > 0:
      self.bright = self.bright - 1

  def show(self):
    print(f"State : {'on' if self.on else 'off'}")
    if self.on:
      print(f"Brightness : {self.bright}")


# TV class
class TV():
 def __init__(self):
  self.isOn = False
  self.isMuted = False
  # Some default list of channels
  self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44,54, 65]
  self.nChannels = len(self.channelList)
  self.channelIndex = 0
  self.VOLUME_MINIMUM = 0 # constant
  self.VOLUME_MAXIMUM = 10 # constant
  self.volume = self.VOLUME_MAXIMUM /2 # integerdivide
 def power(self):
  self.isOn = not self.isOn # toggle
 def volumeUp(self):
  if not self.isOn:
   return
  if self.isMuted:
   self.isMuted = False # changing the volume while muted unmutes the sound
  if self.volume < self.VOLUME_MAXIMUM:
   self.volume = self.volume + 1
 def volumeDown(self):
  if not self.isOn:
   return
  if self.isMuted:
   self.isMuted = False # changing the volume whilemuted unmutes the sound
  if self.volume > self.VOLUME_MINIMUM:
   self.volume = self.volume - 1
 def channelUp(self):
  if not self.isOn:
   return
  self.channelIndex = self.channelIndex + 1
  if self.channelIndex > self.nChannels:
   self.channelIndex = 0 # wrap around to the first channel
 def channelDown(self):
  if not self.isOn:
   return
  self.channelIndex = self.channelIndex - 1
  if self.channelIndex < 0:
   self.channelIndex = self.nChannels - 1 # wrap around to the top channel
 def mute(self):
  if not self.isOn:
   return
  self.isMuted = not self.isMuted
 def setChannel(self, newChannel):
  if newChannel in self.channelList:
   self.channelIndex = self.channelList.index(newChannel)
   # if the newChannel is not in our list of channels,don't do anything
 def showInfo(self):
  print()
  print('TV Status:')
  if self.isOn:
   print(' TV is: On')
   print(' Channel is:', self.channelList[self.channelIndex])
   if self.isMuted:
    print(' Volume is:', self.volume, '(sound is muted)')
   else:
    print(' Volume is:', self.volume)
  else:
   print(' TV is: Off')

#creating an object from the class
#light = LightSwitch()

#call the object method
#light.turnOn()
#light.show()
#light.turnOff()
#light.show()

light = dimmer()

light.turnOn()
light.show()
light.dimUp()
light.show()
light.dimUp()
light.dimUp()
light.show()
light.turnOff()
light.show()
light.turnOn()
light.show()
light.dimDown()
light.show()

tele = TV()
tele.power()
tele.showInfo()
