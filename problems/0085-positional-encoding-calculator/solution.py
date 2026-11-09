import numpy as np

def pos_encoding(position: int, d_model: int):
	# Your code here
	if position == 0 or d_model <=0:
		return -1
	pos_encoding = np.zeros((position,d_model))

	for pos in range(position):
		for i in range(0,d_model,2):
			angle = pos / np.power(10000,i/d_model)
			pos_encoding[pos,i]=np.sin(angle)
			if i+1<d_model:
				pos_encoding[pos, i+1]=np.cos(angle)


	pos_encoding = np.float16(pos_encoding)
	return pos_encoding