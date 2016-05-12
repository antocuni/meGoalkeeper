import cv2

class Player(object):

    def __init__(self, src, winname='frame', show=True,
                 filename='/tmp/frame.png'):
        self.src = src
        self.winname = winname
        self.show = show
        self.filename = filename
        cv2.namedWindow(winname)

    def process(self, frame):
        return frame

    def run(self):
        save_next = False
        while True:
            frame = self.src.read()
            if save_next:
                print 'Saving frame to', self.filename
                cv2.imwrite(self.filename, frame)
                save_next = False
            #
            frame = self.process(frame)

            if self.show:
                cv2.imshow(self.winname, frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break
                if key == ord('s'):
                    save_next = True
                    frame = camera.read()
                    cv2.imwrite("/tmp/frame.png", frame)


if __name__ == '__main__':
    from goalkeeper.camera import CVCamera
    camera = CVCamera(640, 480)
    player = Player(camera)
    player.run()
