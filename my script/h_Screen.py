# -*- coding: utf-8 -*-
class Screen(object):
	@property
	def width(self):
		return self._width
		
	@width.setter	
	def width(self,width):
		if not isinstance(width,int):
			raise ValueError('width must be int type')
		self._width = width		
		
	@property	
	def height(self):
		return self.height
		
	@height.setter	
	def height(self,height):	
		if not isinstance(height,int):
			raise ValueError('height must be int type')	
		self._height = height
		
	@property	
	def resolution(self):
		return self._height * self._width

		
# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution		