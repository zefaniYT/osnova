import os.path
from flask import Flask, request, jsonify, send_from_directory
from variants.ManagerPlace import CountryManager, CityManager, HotelManager
import mysql.connector
from mysql.connector import Error                                                       #обработка ошибок и исключений
import config
