#!/usr/bin/env python3
# coding:utf-8
import asyncio
import aiomysql

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test_example():
	conn = yield from aiomysql.connect(host='10.1.64.80',port=9035,user='healthcloud',password='healthcloud123456',db='vaccine_server_core',loop=loop)
	cur = yield from conn.cursor()
	yield from cur.execute("select id,nickname,mobile from tb_account_user")
	print(cur.description,'---------------------------')
	print(r)	
	yield from cur.close()
	conn.close
	
loop.run_until_complete(test_example())	