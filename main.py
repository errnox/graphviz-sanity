import graphviz


class App(object):
  def __init__(self):
    self.graph = graphviz.Digraph(
      name='graph', format='png', node_attr={'shape': 'box'})

    self.nodes = {
      'pete':    'Pete Smith',
      'ann':     'Ann Miller',
      'derek':   'Derek Bowy',
      'penny':   'Penny Smarts',
      'lindsay': 'Lindsay Miller',
      }

    self.edges = [
      ('pete',  'ann',     {'label': 'knows'                         }),
      ('ann',   'lindsay', {'label': 'know each other', 'dir': 'both'}),
      ('derek', 'ann',     {'label': 'has met'                       }),
      ('derek', 'pete',    {'label': 'knows'                         }),
      ('pete',  'derek',   {'label': 'has heard of'                  }),
      ('penny', 'pete',    {'label': 'knows'                         }),
      ]

  def run(self):
    for k, v in self.nodes.iteritems():
      self.graph.node(k, v)

    for edge in self.edges:
      self.graph.edge(edge[0], edge[1], **edge[2])

    self.graph.render()


if __name__ == '__main__':
  app = App()
  app.run()
