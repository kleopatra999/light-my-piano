"""Mock version of piano_input.PianoInput.
For use when testing on a computer without an actual MIDI input.

Copyright 2015 Google Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import Queue

class PianoInput(object):
  def __init__(self):
    self.user_input = Queue.Queue()
    for note in xrange(37,90):
      self.user_input.put((note, 45))

  def ClearInput(self):
    while not self.user_input.empty():
      self.user_input.get()
