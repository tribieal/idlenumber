import cherrypy, commands,os,urllib2,json,urllib,time

localtime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
print localtime

def _post_xa(events):
    url = "http://analytic.337.com/v3/index.php"        
    params = {"json": json.dumps({"signedParams":{"appid": "cloud-cloud",                                                      "uid": "random"},                                      "stats": events})} 
    data = urllib.urlencode(params)        
    req = urllib2.Request(url, data)        
    print "data is"
    print data
    response = urllib2.urlopen(req)        
    return response.read()



#euca2 vm15
node = "ssh vm15.xingcloud.com /usr/bin/euca-describe-availability-zones verbose |grep m1.xlarge|awk '{print $4}'"
java2 = commands.getstatusoutput(node)[1]

node = "ssh vm15.xingcloud.com /usr/bin/euca-describe-availability-zones verbose |grep medium|awk '{print $4}'"
php2 = commands.getstatusoutput(node)[1]


#euca1 nm
node = "ssh nm.xingcloud.com /usr/bin/euca-describe-availability-zones verbose |grep m1.xlarge|awk '{print $4}'"
java1 = commands.getstatusoutput(node)[1]

node = "ssh nm.xingcloud.com /usr/bin/euca-describe-availability-zones verbose |grep medium|awk '{print $4}'"
php1 = commands.getstatusoutput(node)[1]



#euca3 vm11
#node = "ssh vm11.xingcloud.com /usr/bin/euca-describe-availability-zones verbose |grep m1.xlarge|awk '{print $4}'"
#java3 = commands.getstatusoutput(node)[1]
#
#node = "ssh vm11.xingcloud.com /usr/bin/euca-describe-availability-zones verbose |grep medium|awk '{print $4}'"
#php3 = commands.getstatusoutput(node)[1]
#
#
#
##euca4 vm16
#node = "ssh vm16.xingcloud.com /usr/bin/euca-describe-availability-zones verbose |grep m1.xlarge|awk '{print $4}'"
#java4 = commands.getstatusoutput(node)[1]
#
#node = "ssh vm16.xingcloud.com /usr/bin/euca-describe-availability-zones verbose |grep medium|awk '{print $4}'"
#php4 = commands.getstatusoutput(node)[1]


#sum of euca1.2.3.4
java = int(java1)+int(java2)
java = str(java)
php = int(php1)+int(php2)
php = str(php)




#print 'java1'+str(java1) + 'java2'+str(java2) + 'java3'+str(java3) +'java4'+str(java4)


print 'java'+str(java)+'php'+str(php)


output2allnode_txt = "#Eucalyptus#"+" php:"+str(php)+" java:"+str(java)
print output2allnode_txt 


idlenumber = range(10)
idlenumber[0] = {"eventName":"euca.cn.java.sum","value":java}
idlenumber[1] = {"eventName":"euca.cn.java.euca1","value":java1}
idlenumber[2] = {"eventName":"euca.cn.java.euca2","value":java2}
#idlenumber[3] = {"eventName":"euca.cn.java.euca3","value":java3}
#idlenumber[4] = {"eventName":"euca.cn.java.euca4","value":java4}
idlenumber[5] = {"eventName":"euca.cn.php.sum","value":php}
idlenumber[6] = {"eventName":"euca.cn.php.euca1","value":php1}
idlenumber[7] = {"eventName":"euca.cn.php.euca2","value":php2}
#idlenumber[8] = {"eventName":"euca.cn.php.euca3","value":php3}
#idlenumber[9] = {"eventName":"euca.cn.php.euca4","value":php4}


print "idlenumberorigin"
print idlenumber
print _post_xa(idlenumber)


