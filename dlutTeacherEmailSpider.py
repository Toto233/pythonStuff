import io
import sys
import urllib
import urllib.parse
import urllib.request
from urllib.parse import urlencode
from bs4 import BeautifulSoup as bs
from requests.exceptions import RequestException

import requests
import re
import json




root_url = 'http://faculty.dlut.edu.cn'
urls = [
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=1&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=2&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=3&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=4&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=5&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=6&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=7&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=8&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=9&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=10&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=11&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=12&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=13&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=14&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=15&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=16&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=17&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=18&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=19&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=20&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=21&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=22&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=23&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=24&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=25&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=26&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=27&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=28&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=29&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=30&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=31&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=32&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=33&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=34&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=35&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=36&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=37&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=38&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=39&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=40&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=41&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=42&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=43&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=44&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=45&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=46&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=47&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=48&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=49&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=50&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=51&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=52&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=53&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=54&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=55&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=56&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=57&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=58&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=59&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=60&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=61&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=62&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=63&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=64&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=65&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=66&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=67&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=68&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=69&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=70&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=71&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=72&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=73&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=74&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=75&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=76&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=77&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=78&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=79&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=80&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=81&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=82&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=83&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=84&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=85&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=86&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=87&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=88&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=89&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=90&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=91&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=92&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=93&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=94&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=95&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=96&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=97&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=98&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=99&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=100&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=101&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=102&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=103&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=104&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=105&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=106&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=107&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=108&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=109&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=110&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=111&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=112&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=113&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=114&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=115&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=116&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=117&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=118&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=119&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=120&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=121&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=122&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=123&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=124&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=125&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=126&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=127&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=128&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=129&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=130&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=131&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=132&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=133&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=134&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=135&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=136&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=137&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=138&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=139&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=140&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=141&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=142&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=143&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=144&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=145&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=146&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=147&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=148&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=149&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=150&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=151&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=152&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=153&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=154&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=155&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=156&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=157&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=158&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=159&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=160&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=161&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=162&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=163&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=164&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=165&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=166&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=167&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=168&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=169&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=170&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=171&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=172&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=173&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=174&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=175&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=176&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=177&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=178&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=179&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=180&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=181&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=182&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=183&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=184&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=185&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=186&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=187&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=188&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=189&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=190&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=191&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=192&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=193&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=194&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=195&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=196&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=197&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=198&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=199&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=200&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=201&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=202&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=203&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=204&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=205&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=206&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=207&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=208&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=209&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=210&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=211&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=212&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=213&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=214&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=215&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=216&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=217&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=218&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=219&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=220&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=221&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=222&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=223&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=224&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=225&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=226&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=227&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=228&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=229&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=230&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=231&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=232&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=233&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=234&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=235&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=236&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=237&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=238&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=239&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=240&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=241&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=242&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=243&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=244&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=245&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=246&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=247&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=248&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=249&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=250&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=251&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=252&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=253&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=254&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=255&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=256&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=257&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=258&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=259&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=260&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=261&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=262&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=263&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=264&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=265&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=266&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=267&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=268&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=269&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=270&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=271&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=272&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=273&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=274&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=275&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    '//xylb--jiaoshi.jsp?totalpage=276&PAGENUM=276&urltype=tsites.CollegeTeacherList&wbtreeid=1035&st=0&id=1143&lang=zh_CN',
    ]


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def run(content):
    try:
        url = 'http://faculty.dlut.edu.cn/system/resource/tsites/tsitesencrypt.jsp'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                        'Content-Type':'application/x-www-form-urlencoded'
        }
        data = {"id":"_tsites_encryp_tsteacher_tsemail",
                "content":content,
                "mode":"8"}
        query_string = urllib.parse.urlencode( data )   
        #print (url+'?'+query_string)

        req = urllib.request.Request(url+'?'+query_string)
        
        

        req.headers = headers

        resp_text = urllib.request.urlopen(req).read().decode('UTF-8')
        json_obj = json.loads(resp_text)
        return json_obj['content']
    except RequestException:
        return None

def find_teacher(url):
    response = requests.get(url, headers=headers)
    #aicongfang@dlut.edu.cn
    page = bs(response.text, 'html.parser')
    encContent = page.select('#_tsites_encryp_tsteacher_tsemail')
    if not encContent:
        return None
    email = run(encContent[0].get_text())
    return  email

def find_teacher_list(url):
    response = requests.get(root_url+url, headers=headers)
    page = bs(response.text, 'html.parser')
    teacher_list = page.select(' ul > li > span')
   
    with open('teacher.txt', 'a') as f:
        for teacher in teacher_list:
            teacherInfo = teacher.get_text().replace('\n\n','\n').replace('\n',',').split(',')[1:]
            name = teacherInfo[0]
            college = teacherInfo[1]
            title = teacherInfo[2]
            if not teacher.a:
                continue
            email = find_teacher(teacher.a['href'])
            f.write(f'{college}')
            f.write(f'\t{name}')
            f.write(f'\t{title}')
            f.write(f'\t{email}')
            print(name,email)
            f.write('\n')



for url in urls:
    find_teacher_list(url)
