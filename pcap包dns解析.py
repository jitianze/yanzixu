#!/usr/bin/python
#-*-coding:utf-8-*-
import struct
import dpkt
import sys
import socket
import binascii
import os

#mulu =raw_input("Please enter the directory you want to parse：")
DNS_A = 1    # RR types
DNS_IN = 1   # RR classes
def addr2str(addrobj):
    if len(addrobj) != 4:
        return "addr error!"
    else:
        return str(ord(addrobj[0]))+"."+str(ord(addrobj[1]))+"."+str(ord(addrobj[2]))+"."+str(ord(addrobj[3]))

def dns_response_body_parse(body):        # parse the response message's body
    identification = body[0:2]
    flag = body[2:4]
    num_ques = body[4:6]
    num_ans_RR = body[6:8]
    num_auth_RR = body[8:10]
    num_addi_RR = body[10:12]
    query_name = ''
    ans_ip = []
    flag = 12
    while(ord(body[flag])!=0x0):
        query_name = query_name + body[flag+1:flag+ord(body[flag])+1]
        flag = flag + ord(body[flag]) + 1
        try:
            if ord(body[flag]) != 0x0:
                query_name = query_name+'.'
        except Exception, e:
            print "error when parse query domain name"
    #print query_name
    flag = flag + 1
    query_type = ord(body[flag])*256 + ord(body[flag+1])
    if query_type == 0x01:            # use domain query IP addr
        flag = flag + 4
        i = 1
        answer_num = ord(num_ans_RR[0])*256 + ord(num_ans_RR[1])
        while(i<=answer_num):
            if ord(body[flag]) == 0xc0:
                flag = flag + 2
            else:
                while(ord(body[flag])!=0x0):
                    flag = flag + ord(body[flag]) + 1
                flag = flag + 1
            if (    ord(body[flag])*256+ord(body[flag+1]) == DNS_A 
                and ord(body[flag+2])*256+ord(body[flag+3]) == DNS_IN):
                flag = flag + 8
                RR_data_len = ord(body[flag])*256 + ord(body[flag+1])
                if RR_data_len == 4:
                    ans_ip.append(addr2str(body[flag+2:flag+6]))
                flag = flag + ord(body[flag])*256 + ord(body[flag+1]) + 2
            else:
                flag = flag + 8
                flag = flag + ord(body[flag])*256 + ord(body[flag+1]) + 2
            i = i + 1
    else:
        print "query type is PTR not A"
        print ("Finished, the result was in file dns-message.txt ")
        return
    return "%s\t%s"%(query_name,ans_ip)

def jiexi():
    def GetFileList(dir, fileList):
        newDir = dir
        if os.path.isfile(dir):
            fileList.append(dir.decode('gbk'))
        elif os.path.isdir(dir):  
            for s in os.listdir(dir):
                newDir=os.path.join(dir,s)
                GetFileList(newDir, fileList)  
        return fileList
    mulu =raw_input("Please enter the directory you want to parse:")
    wenjianlist = GetFileList(mulu, [])
    #list 现在是一个文件路径的列表
    nr_list=[]
    for i in wenjianlist:
        a=file(i,"rb")
        nr_list.append(a) 
    f_xieru = open("C:\Users\jitianze\Desktop\dns_message.txt","a")
    #fw_list = map(file("for i in list","rb"),list)

    for fw_list in nr_list:
        pcap = dpkt.pcap.Reader(fw_list)
        for ts,buf in pcap:
            ethheader = buf[0:14]
            dstmac = ethheader[0:6]
            srcmac = ethheader[6:12]
            netlayer_type = ethheader[12:14]

            pktheader = buf[14:34]
            trans_type = pktheader[9]
            srcip = pktheader[12:16]
            dstip = pktheader[16:20]

            if (ord(trans_type) == 0x11):     #UDP
                udpheader = buf[34:42]
                srcport = udpheader[0:2]
                dstport = udpheader[2:4]
                udplen = udpheader[4:6]

                bodylen = ord(udplen[0])*256+ord(udplen[1])-8
                dnsbody = buf[42:(42+bodylen)]
                if (ord(dstport[0]) == 0x00 and ord(dstport[1]) == 0x35):
                    print "this stream has a DNS Request"
                elif (ord(srcport[0]) == 0x00 and ord(srcport[1]) == 0x35):
                    print "this stream has a DNS Response"

                    # try:
                    # print "dnsbody:", dnsbody
                    jibangb = dns_response_body_parse(dnsbody)
                    print 'this is result:', jibangb
                    if jibangb != None:
                    	f_xieru.write(jibangb + '\n')
                    else:
                    	print "ibangb is none ..", jibangb
                    # f_xieru.writelines(dns_response_body_parse(dnsbody))    # wirte result to file
                	# except:
                		# print u"文件读取有误，捕获异常："
                else:
                    print "this stream has not dns"
            elif (ord(trans_type) == 0x06):     #TCP
                tcpheader = buf[34:54]
                srcport = tcpheader[0:2]
                dstport = tcpheader[2:4]               
    print ("Finished, the result was in file dns-message.txt ")
    f_xieru.close()
    
if __name__ == "__main__":
    jiexi()

 # 推荐几个学习网站 www.baidu.com
 # 你差我3k