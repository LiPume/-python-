import asyncio
import json
import sys
import os

from src import data_object

current_path = os.path.abspath(__file__)
top_path = '\\'.join(current_path.split('\\')[:-2])
sys.path.append(top_path)
from share.const import *
from const import *
import pymysql
import src.data_object

class Game(object):
    def __init__(self):
        self.plantInfo = [[0]*GRID_COUNT[1] for _ in range(GRID_COUNT[0])]
        self.connectMysql()
        self.loadPlantInfo()
        self.gold = 100

    def connectMysql(self):
        config = {
            'host' : DB_HOST,
            'port' : DB_PORT,
            'user' : DB_USER,
            'password' : DB_PASS,
            'db' : 'pvzdb',
            'charset' : 'utf8mb4'
        }
        try:
            self.connect = pymysql.connect(**config)
            print('connect mysql succeed!')
        except pymysql.err.OperationalError as e:
            print('connect mysql failed!')
            print('Error:', e)

    def executeSql(self, sqlCmd, params=None):
        cursor = self.connect.cursor()
        try:
            if params:
                cursor.execute(sqlCmd, params)
            else:
                cursor.execute(sqlCmd)
            self.connect.commit()
            results = cursor.fetchall()
            return results
        except Exception as e:
            print(f"SQL执行失败! 错误: {e}")
            self.connect.rollback()
            return None
        finally:
            cursor.close()

    def loadPlantInfo(self):
        results = self.executeSql("select * from game;")
        if len(results) == 0:
            self.savePlantInfo()
        else:
            print(results[0][0])
            self.plantInfo = json.loads(results[0][0])


    def savePlantInfo(self):
        plantInfo_str = json.dumps(self.plantInfo)
        sql = "insert into game(id,plantInfo) values (0,%s) on duplicate key update id = 0,plantInfo = %s;"
        self.executeSql(sql, (plantInfo_str, plantInfo_str))

    def checkAddPlant(self,pos,plantIdx):
        msg = {
            'type' : S2C_ADD_PLANT,
            'code' : S2C_CODE_FAILED,
            'pos' :pos,
            'plant_idx' :plantIdx,
            'gold' : self.gold,
        }
        x,y = pos
        if x < 0 or x >= GRID_COUNT[0]:
            return msg
        if y < 0 or y >= GRID_COUNT[1]:
            return msg
        if self.plantInfo[x][y] != 0:
            return msg
        if self.gold < data_object.data[plantIdx]['PRICE']:
            return
        self.gold -= data_object.data[plantIdx]['PRICE']
        self.plantInfo[x][y] = plantIdx
        self.savePlantInfo()
        msg['code'] = S2C_CODE_SUCCEED
        msg['gold'] = self.gold
        return msg

    def getPlantInfo(self):
        msg = {
            'type' : S2C_GET_PLANT,
            'code' : S2C_CODE_SUCCEED,
            'plant_info' : self.plantInfo,
        }
        return msg

