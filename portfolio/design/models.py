from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

# COLORS small average large counts color

pink = 'pink'
indigo = 'indigo'
cyan = 'cyan'
light_green = 'light-green'
amber = 'amber'
brown = 'brown'
white = 'white'
grey = 'grey'
black = 'black'

COLOR_SMALL = {'pink': pink,
               'indigo': indigo,
               'cyan': cyan,
               'light-green': light_green,
               'amber': amber,
               'brown': brown,
               'white': white,
               'grey': grey,
               'black': black,
               }

# COLORS TEXT grey-text

text = 'text'

COLOR_TEXT_SMALL = {'pink': '{}-{}'.format(pink, text),
                    'indigo': '{}-{}'.format(indigo, text),
                    'cyan': '{}-{}'.format(cyan, text),
                    'light-green': '{}-{}'.format(light_green, text),
                    'amber': '{}-{}'.format(amber, text),
                    'brown': '{}-{}'.format(brown, text),
                    'white': '{}-{}'.format(white, text),
                    'grey': '{}-{}'.format(grey, text),
                    'black': '{}-{}'.format(black, text),
                    }


# ALIGN left-align

align = 'align'
center = 'center'
right = 'right'
left = 'left'

ALIGN = {'center': '{}-{}'.format(center, align),
         'right': '{}-{}'.format(right, align),
         'left': '{}-{}'.format(left, align)
         }
