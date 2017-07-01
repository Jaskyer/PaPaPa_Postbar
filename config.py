# -*- coding:utf-8 -*-
import os
import re
import urllib

#url = 'http://tieba.baidu.com/f?kw=%E7%9B%96%E5%B0%94%E5%8A%A0%E6%9C%B5&ie=utf-8'
url = 'http://tieba.baidu.com/f?kw=%E8%8E%8E%E6%8B%89%E5%A4%8F%E5%B8%8C&ie=utf-8'
#acter = 'GalGadot'
acter = 'SarahShahi'

headers = {"Accept":"0text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.8",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
"Host":"tieba.baidu.com",
"Pragma":"no-cache",
"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}


'''headers = {"Accept":"0text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch",
"Cache-Control":"no-cache",
"Cookie":"TIEBA_USERTYPE=f5b3af106949be594c46107e; bdshare_firstime=1496919944526; FP_UID=3ecf28a55be6cf1bbd4add8f670ed5c8; BAIDUID=8A3E2A0EEAD19A5A1048F24D81CCB84F:FG=1; PSTM=1496921490; BIDUPSID=508781D681D9E2A583442D91782CA9B8; bottleBubble=1; BDSFRCVID=6J4sJeC62ZL3kATZhFQargemaWVpeAbTH6aIvRKa_j5dWTiWApZbEG0PqU8g0KubKDHsogKK3gOTH4nP; H_BDCLCKID_SF=tJAO_D0yJK03qn5zqRbsMt-0-fTMa-Q8HD7yWCkKWDb5OR5Jj65AX5tfLJOzaU5IK6rM0R6qQMQ2eqjP3MA--fFB04RKy-It5NvnBx3p-UcDsq0x0bQle-bQypoaBM37-KOMahkb5h7xOKbk056jK4JKDGteJj3P; wise_device=0; BDUSS=VBrUnpGbHg4MUFEYk9EQlVaWTRLNkprLThtb3VpV01hNHB4M1ppcVpSRVphR2RaSVFBQUFBJCQAAAAAAAAAAAEAAADKU-IpTHlfvvW3xwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABnbP1kZ2z9ZZ; STOKEN=0908de3f5d6af8e045a31b30004b08b5a46335cc913171025a2c5eace137c17a; TIEBAUID=5e2d54c3bf97b3494cd40373; fixed_bar=1; FP_LASTTIME=1497437774204; 702698442_FRSVideoUploadTip=1; BDRCVFR[Mi2iENwDnGn]=9xWipS8B-FspA7EnHc1QhPEUf; PSINO=6; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0",
"Connection":"keep-alive",
"Host":"tieba.baidu.com",
"Pragma":"no-cache",
"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}'''