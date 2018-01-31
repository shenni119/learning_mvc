import pygame
import view
import model
from button import Button


BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (127, 127, 127)

RED = (255, 0, 0)


class Datachangebutton(Button):
    def __init__(self, text, rect):
        Button.__init__(self, text, rect)
        # self.chart = chart
        # self.btype=btype
        # self.party = 'gop'
        # self.percent=False
        # self.decending=False
        # self.color=GRAY

    # def on_click(self, event):
    #     currentparty='dem'
    #     currentraw=True
    #     currentsort=True
    #     if self.btype=='party':
    #         if self.party=='dem':
    #             currentparty='dem'
    #             self.color=RED
    #             # self.party = 'gop'
    #         else:
    #             currentparty='gop'
    #             # self.party = 'dem'
    #
    #     if self.btype=='sort':
    #         if (self.decending):
    #             currentsort=True
    #             self.decending = False
    #         else:
    #             currentsort = False
    #             self.decending=True
    #     if self.btype=='percent':
    #         if (self.percent):
    #             currentraw=True
    #             self.percent = False
    #         else:
    #             currentraw=False
    #             self.percent = True
    #
    #     data = model.get_data(currentparty, currentraw, currentsort)
    #     self.chart.set_values(data)


pygame.init()

screen = pygame.display.set_mode((1200, 600))

pygame.display.set_caption("Election Data Viewer")
pygame.display.update()


screen_rect = screen.get_rect()
bc_rect = pygame.Rect(screen_rect.x, screen_rect.y, screen_rect.width, screen_rect.height) # make it the full height again

# print (data)

dembutton = Datachangebutton("Dem", pygame.Rect(10, screen_rect.height - 70, 100, 30))
gopbutton = Datachangebutton("Gop", pygame.Rect(10, screen_rect.height - 40, 100, 30))
upbutton= Datachangebutton("Up", pygame.Rect(200, screen_rect.height - 70, 100, 30))
downbutton= Datachangebutton("Down", pygame.Rect(200, screen_rect.height - 40, 100, 30))
rawbutton= Datachangebutton("Raw", pygame.Rect(390, screen_rect.height - 70, 100, 30))
percentbutton= Datachangebutton("%", pygame.Rect(390, screen_rect.height - 40, 100, 30))

# percentbutton=

currentparty='dem'
currentraw=True
currentsort=True
colordem=RED
colorgop=GRAY
colorraw=RED
colorpercent=GRAY
colorup=RED
colordown=GRAY
# display loop
done = False
while not done:
    screen.fill(view.BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            if gopbutton.handle_event(event)==1:
                currentparty='gop'
                colorgop=RED
                colordem=GRAY
            if dembutton.handle_event(event)==1:
                currentparty='dem'
                colorgop=GRAY
                colordem=RED
            if rawbutton.handle_event(event)==1:
                currentraw=True
                colorraw=RED
                colorpercent=GRAY
            if percentbutton.handle_event(event)==1:
                currentraw=False
                colorraw=GRAY
                colorpercent=RED
            if upbutton.handle_event(event)==1:
                currentsort=True
                colorup=RED
                colordown=GRAY
            if downbutton.handle_event(event)==1:
                currentsort=False
                colorup=GRAY
                colordown=RED
            # sortbutton.handle_event(event)
            data = model.get_data(currentparty, currentraw, currentsort)
            bc = view.BarChart(screen.get_rect(), data)
    bc.draw(screen)
    dembutton.draw(screen,colordem)
    gopbutton.draw(screen,colorgop)
    upbutton.draw(screen, colorup)
    downbutton.draw(screen, colordown)
    rawbutton.draw(screen, colorraw)
    percentbutton.draw(screen,colorpercent)
    pygame.display.update()



# class Datachangebutton:
# 	def __init__(self, text, rect, chart):
#
#         self.text = text
#         self.rect = rect
#         self.chart=chart
#         self.gop = False
#
#     def on_click(self, event):
#         # we will just toggle between sorted and unsorted data
#         if (self.gop):
#             data = model.get_data()
#             self.gop = False
#         else:
#             data = model.get_data(party='gop')
#             self.gop = True
#
# 	def draw(self, surface):
# 		pygame.draw.rect(surface, GRAY, self.rect)
#
# 		font = pygame.font.Font(None, 36)
# 		label_view = font.render(self.text, False, BLACK)
# 		label_pos = label_view.get_rect()
# 		label_pos.centery = self.rect.centery
# 		label_pos.centerx = self.rect.centerx
# 		surface.blit(label_view, label_pos)
#
# 	def handle_event(self, event):
# 		if event.type == pygame.MOUSEBUTTONDOWN:
# 			(x, y) = pygame.mouse.get_pos()
# 			if x >= self.rect.x and \
# 				x <= self.rect.x + self.rect.width and \
# 				y >= self.rect.y and \
# 				y <= self.rect.y + self.rect.height:
#
# 				self.on_click(event)
#
# 	# def on_click(self, event):
# 	# 	print("button clicked")
#
#
#         # if (self.decending):
#         #     data = model.get_data()
#         #     self.decending=False
#         # else:
#         #     data = model.get_data(sort_ascending=False)
#         #     self.decending=True
#         self.chart.set_values(data)
