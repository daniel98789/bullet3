import time

def object_is_in_frame(p, obj_id, prev_loc = None):
	# get current view of the debug visualizer camera
	start = time.time()
	cam_info = p.getDebugVisualizerCamera()
	# get camera image based on DV info
	img = p.getCameraImage(cam_info[0], cam_info[1], cam_info[2], cam_info[3])
	seg = img[4]
	if prev_loc is not None:
		# check prev location found for the object to save on query
		# TODO: check a surrounding area
		found, loc = check_area(seg, prev_loc, obj_id)
		if found:
			return True, loc

	# print(cam_info[3])
	# p.resetDebugVisualizerCamera( cameraDistance=x, cameraYaw=40, cameraPitch=-30, cameraTargetPosition=[0,0,0])
	for x, pixel in enumerate(seg):
		for y, val in enumerate(pixel):
			if check_pixel(val, obj_id):
				return True, [x, y]
	return False, None

CACHED_SEARCH_SIZE = 20
def check_area(img, prev_loc, obj_id):
	# check a 50*50 area near the prev_loc in case it moved since last check
	x_range = [max(0, prev_loc[0] - CACHED_SEARCH_SIZE//2), min(len(img) - 1, prev_loc[1] + CACHED_SEARCH_SIZE//2)]
	y_range = [max(0, prev_loc[1] - CACHED_SEARCH_SIZE//2), min(len(img[0]) - 1, prev_loc[1] + CACHED_SEARCH_SIZE//2)]
	for x in range(x_range[0], x_range[1] + 1):
		for y in range(y_range[0], y_range[1] + 1):
			if check_pixel(img[x][y], obj_id):
				return True, [x, y]
	return False, None

def check_pixel(pixel, obj_id):
	if pixel >= 0:
		obUid = pixel & ((1 << 24) - 1)
		if obUid == obj_id:
			# TODO: take note of indices for caching
			return True
	return False