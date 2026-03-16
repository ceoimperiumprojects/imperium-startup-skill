"""Imperium Brain Carousel Cookbook — 21 slide layouts for python-pptx.

Each layout is a standalone function that adds a single slide to a Presentation
object. All functions share the same signature:

    add_slide(prs, title="", body="", colors=None, fonts=None, **kwargs)

Import layouts by name:
    from cookbook import title_centered, content_bullets, cta_slide
    title_centered(prs, title="Hello World")
"""

# --- Title layouts (4) ---
from .title_centered import add_slide as title_centered
from .title_bold import add_slide as title_bold
from .title_image import add_slide as title_image
from .title_gradient import add_slide as title_gradient

# --- Content layouts (8) ---
from .content_single import add_slide as content_single
from .content_bullets import add_slide as content_bullets
from .content_two_column import add_slide as content_two_column
from .content_quote import add_slide as content_quote
from .content_stats import add_slide as content_stats
from .content_comparison import add_slide as content_comparison
from .content_timeline import add_slide as content_timeline
from .content_checklist import add_slide as content_checklist

# --- Image layouts (4) ---
from .image_full import add_slide as image_full
from .image_left import add_slide as image_left
from .image_right import add_slide as image_right
from .image_grid import add_slide as image_grid

# --- Data layouts (3) ---
from .data_bar_chart import add_slide as data_bar_chart
from .data_pie_chart import add_slide as data_pie_chart
from .data_table import add_slide as data_table

# --- Special layouts (2) ---
from .cta_slide import add_slide as cta_slide
from .divider_slide import add_slide as divider_slide

# All layouts indexed by name for programmatic access
ALL_LAYOUTS = {
    'title_centered': title_centered,
    'title_bold': title_bold,
    'title_image': title_image,
    'title_gradient': title_gradient,
    'content_single': content_single,
    'content_bullets': content_bullets,
    'content_two_column': content_two_column,
    'content_quote': content_quote,
    'content_stats': content_stats,
    'content_comparison': content_comparison,
    'content_timeline': content_timeline,
    'content_checklist': content_checklist,
    'image_full': image_full,
    'image_left': image_left,
    'image_right': image_right,
    'image_grid': image_grid,
    'data_bar_chart': data_bar_chart,
    'data_pie_chart': data_pie_chart,
    'data_table': data_table,
    'cta_slide': cta_slide,
    'divider_slide': divider_slide,
}

__all__ = list(ALL_LAYOUTS.keys()) + ['ALL_LAYOUTS']
