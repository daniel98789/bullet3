import pybullet as p
import time


class Profiler:
	def __init__(self,bullet_client,bodyUniqueIDList):
		self.prev_count = 0
		self.frameCounter = 0
		self.update_interval = 1.44
		self.p=bullet_client
		self.bodies = bodyUniqueIDList
		self.start_time = time.time()

	def select_object_to_get_pos_ori(self,bodyUniqueID):
		self.pos_obj = bodyUniqueID


	def profile(self,profile_mask):
		self.frameCounter += 1

		self.curr_time = time.time()
		if self.curr_time - self.start_time > self.update_interval:
			self.start_time = self.curr_time

			
			if (profile_mask & (1<<0)):
				self.p.addUserDebugText("FPS: " + "{:.2f}".format((self.frameCounter - self.prev_count)/self.update_interval), [10, 2, -0.4],
						textColorRGB=[0, 0, 0],
						textSize=1.3,
						lifeTime=self.update_interval+0.1)
			self.prev_count = self.frameCounter

			if (profile_mask & (1<<1)):
				numJoints = 0
				for ID in self.bodies:
					numJoints += self.p.getNumJoints(ID)

				self.p.addUserDebugText("Joint Count: " + str(numJoints), 
							[10, -0.5, -1.55],
							textColorRGB=[0, 0, 0],
							textSize=1.3,
							lifeTime=self.update_interval+0.1)

			if (profile_mask & (1<<2)):
				position = self.p.getBasePositionAndOrientation(self.pos_obj)

				self.p.addUserDebugText("Position: " + "x: " + "{:.2f}".format(position[0][0]) + " y: " + "{:.2f}".format(position[0][1]) + " z: " + "{:.2f}".format(position[0][2]), 
							[10, 0.5, -1.07],
							textColorRGB=[0, 0, 0],
							textSize=1.3,
							lifeTime=self.update_interval+0.1)
			
			if (profile_mask & (1<<3)):
				self.p.addUserDebugText("Orientation: " "x: " + "{:.2f}".format(position[1][0]) + " y: " + "{:.2f}".format(position[1][1]) + " z: " + "{:.2f}".format(position[1][2]), 
							[10, 0, -1.29],
							textColorRGB=[0, 0, 0],
							textSize=1.3,
							lifeTime=self.update_interval+0.1)

			if (profile_mask & (1<<4)):
				self.p.addUserDebugText("Frame Counter: " + str(self.frameCounter), [10, 1.5, -0.625],
						textColorRGB=[0, 0, 0],
						textSize=1.3,
						lifeTime=self.update_interval+0.1)

			


			if (profile_mask & (1<<5)):
				numBodies = self.p.getNumBodies()
				self.p.addUserDebugText("Body Count: " + str(numBodies), [10, 1, -0.85],
							textColorRGB=[0, 0, 0],
							textSize=1.3,
							lifeTime=self.update_interval+0.1)

			if (profile_mask & (1<<6)):
				cameraPosition = self.p.getDebugVisualizerCamera()
				viewHeight = cameraPosition[0]
				viewWidth = cameraPosition[1]
				yaw = cameraPosition[8]
				pitch = cameraPosition[9]
				dist = cameraPosition[10]
				targetX = cameraPosition[11][0]
				targetY = cameraPosition[11][1]
				targetZ = cameraPosition[11][2]

				self.p.addUserDebugText("View Size: " + str(viewHeight) + "x" + str(viewWidth), 
								[10, -1, -1.77],
								textColorRGB=[0, 0, 0],
								textSize=1.3,
								lifeTime=self.update_interval+0.1)
				
				self.p.addUserDebugText("Yaw: " + str(yaw) + " Pitch: " + str(pitch), 
								[10, -1.5, -1.99],
								textColorRGB=[0, 0, 0],
								textSize=1.3,
								lifeTime=self.update_interval+0.1)

				self.p.addUserDebugText("Camera Distance: " + "{:.2f}".format(dist), 
								[10, -2, -2.22],
								textColorRGB=[0, 0, 0],
								textSize=1.3,
								lifeTime=self.update_interval+0.1)

				self.p.addUserDebugText("Camera Position: x=" + str(targetX) + " y=" + str(targetY) + " z=" + str(targetZ), 
								[10, -2.5, -2.45],
								textColorRGB=[0, 0, 0],
								textSize=1.3,
								lifeTime=self.update_interval+0.1)

