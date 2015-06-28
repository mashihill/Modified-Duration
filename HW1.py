def mdcv(y, c, w):
	MD = PV = CV = 0;

	for i in (range(len(c))):
  		MD += ((w+i)*(c[i])) / (1+y)**(w+i)
   		PV += c[i]/(1+y)**(w+i)
   		CV += (w+i)*(-(w+i)-1)*c[i]/(1+y)**(w+i+2)

	MD = MD/PV/(1+y);
	CV = -CV/PV;
	print 'Modified duration = ' + str(MD)
	print 'Convexity = ' + str(CV)
	return
