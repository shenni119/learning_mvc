import pygame
import numpy
# print math.ceil(4.2)

WHITE = (255,255,255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Bar:
	def __init__(self, color, length, height, padding=0.1):
		self.length = length
		self.color = color
		self.height = height
		self.padding = padding

	def draw(self, surface, x, y):
		padding_height = self.height * self.padding
		adjusted_height = self.height - 2 * padding_height
		pygame.draw.rect(surface, self.color,
		  [x, y + padding_height, self.length, adjusted_height])

class BarChart:

	def __init__(self, rect=pygame.Rect(0,0,600,400), values=[], ticks=10,
		plot_area_width_ratio=0.7, plot_area_height_ratio=0.7, bar_color=GREEN,
		max_val=0):

		self.rect = rect
		self.background = BLACK
		self.label_color = WHITE

		# constant ratios for portions of the display
		self.ticks=ticks
		self.plot_area_width_ratio=plot_area_width_ratio
		self.plot_area_height_ratio=plot_area_height_ratio
		self.label_area_width_ratio = 1.0 - self.plot_area_width_ratio
		self.scale_area_height_ratio = 1.0 - self.plot_area_height_ratio
		self.max_val=max_val
		self.bar_color=bar_color
		self.labelscale=1.1

		self.scale_area = pygame.Rect(
			rect.x + rect.width * self.label_area_width_ratio,
			rect.y + rect.height * self.plot_area_height_ratio,
			rect.width * self.plot_area_width_ratio,
			rect.height * self.scale_area_height_ratio
			)

		self.label_area = pygame.Rect(
			rect.x,
			rect.y,
			rect.width * self.label_area_width_ratio,
			rect.height * self.plot_area_height_ratio
			)

		self.plot_area = pygame.Rect(
			rect.x + self.label_area.width,
			rect.y,
			rect.width * self.plot_area_width_ratio,
			rect.height * self.plot_area_height_ratio
			)

		self.set_values(values)

	def set_values(self, values):
		self.values = values

		# figure out max value
		max_val = 0
		for v in values:
				if v[1] > max_val:
						max_val = v[1]

		self.max_val = max_val

	def get_bar_height(self):
		return self.plot_area.height / len(self.values)

	def draw_labels(self, surface):
		bar_num = 0
		for v in self.values:
			label_text = v[0]
			fontheight=int(self.plot_area.height / (len(self.values)))
			font = pygame.font.Font(None, fontheight)
			label_view = font.render(label_text, False, WHITE)
			label_pos = label_view.get_rect()
			label_pos.centery = self.rect.y + \
			  self.get_bar_height() * bar_num + \
			  self.get_bar_height() / 2
			label_pos.x = self.rect.x + 10
			surface.blit(label_view, label_pos)
			bar_num += 1

	def draw_scale(self, surface):
		scale_label_spacing = self.scale_area.width / self.max_val
		newlst=numpy.arange(0,(self.max_val+1),(self.max_val/self.ticks))
		for i in newlst:
			font = pygame.font.Font(None, 20)
			roundedscale=round(i,2)
			scale_label_view = font.render(str(roundedscale), False, WHITE)
			scale_label_pos = scale_label_view.get_rect()
			scale_label_pos.y = self.scale_area.y + 10
			scale_label_pos.x = self.scale_area.x + \
			  (i * scale_label_spacing/self.labelscale)
			surface.blit(scale_label_view, scale_label_pos)

	def draw_bars(self, surface):
		bar_num = 0
		# colors = [YELLOW, CYAN, MAGENTA, RED, BLUE, GREEN, WHITE]
		for v in self.values:
			bar_length = self.plot_area.width * v[1] / (self.max_val*self.labelscale)
			# b = Bar(colors[bar_num % len(colors)],
			b = Bar(self.bar_color,
			  bar_length,
			  self.plot_area.height / len(self.values))
			y_pos = self.plot_area.y + bar_num * b.height
			bar_num += 1
			b.draw(surface, self.plot_area.x, y_pos)

	def draw(self, surface):
		self.draw_bars(surface)
		self.draw_labels(surface)
		self.draw_scale(surface)
