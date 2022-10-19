import numpy as np
theta_spacing = 0.07
phi_spacing = 0.02

R1 = 1 
R2 = 2
K2 = 5
illumination = np.array([*".,-~:;=!*#$@"])
screen_width = 25
screen_height = 25

K1 = screen_width * K2 * 3 / (8 * (R1 + R2))

def main(A=1 , B=1):

	cosA = np.cos(A)
	cosB = np.cos(B)
	sinA = np.sin(A)
	sinB = np.sin(B)

	output = np.full((screen_height , screen_width) , ' ')
	zbuffer = np.zeros((screen_height , screen_width))

	theta = 0.
	while theta < 2*np.pi:
		# theta  = int(theta)
		costheta = np.cos(theta)
		sintheta = np.sin(theta)

		phi = 0.0
		while phi < 2*np.pi:

			# phi = int(phi)
			cosphi = np.cos(phi)
			sinphi = np.sin(phi)

			circlex = R2 + R1*costheta
			circley = R1*sintheta

			x = circlex*(cosB*cosphi + sinA*sinB*sinphi)- circley*cosA*sinB
			y = circlex*(sinB*cosphi - sinA*cosB*sinphi)+ circley*cosA*cosB
			z =K2 + cosA*circlex*sinphi + circley*sinA
			ooz = 1/z

			xp = int(screen_width /2 + K1*ooz*x)
			yp = int(screen_height/2 - K1*ooz*y)
			# L = cosphi*costheta*sinB − cosA*costheta*sinphi − sinA*sintheta+cosB*(cosA*sintheta − cosphi*sinA*sinphi)
			L =cosphi*costheta*sinB - cosA*costheta*sinphi -sinA*sintheta + cosB*(cosA*sintheta - costheta*sinA*sinphi)
			if L>0:
				if ooz > zbuffer[xp , yp]:
					zbuffer[xp,yp] = ooz
					luminence_index = int(L*8)

					output[xp,yp] = illumination[luminence_index]
			phi = phi + phi_spacing	

		# theta = float(theta)
		theta = theta + theta_spacing	


	print(*[" ".join(row) for row in output], sep="\n")
	

if __name__ == '__main__':
	A = 0 
	B = 0
	for _ in range(screen_width*screen_height):
		A+=theta_spacing
		B+=phi_spacing
		print("\x1b[H") 
		main(A , B)
		print("\x1b[H") 
