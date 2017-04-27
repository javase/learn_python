# -*- coding: utf-8 -*-
import unittest
from mydict import Dict

# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承
class TestDict(unittest.TestCase):
	# 以test开头的方法就是测试方法
	def test_init(self):
		d = Dict(a=1,b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
	
	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key,'value')
	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')
		
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value=d['empty']
	def test_attrerror(self):	
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
	# 再次运行测试看看每个测试方法调用前后是否会打印出setUp...和tearDown...
	def setUp(self):
		print('setUp...')
	def tearDown(self):
		print('tearDown...')
		
if __name__=='__main__':
	unittest.main()
	
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.003s

# OK	

# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。

# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。

# 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。

# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。