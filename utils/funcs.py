
def create_nodes_links(array_nodes):
  nodes = {}
  links = {}

  count = 0
  count_links = 0
  # FOR NOS NODES
  for area in array_nodes:
    # CRIANDO NODES
    nodes[count] = { "id": area["id"], "label": area["name"] }
    count = count + 1
    # FOR NAS CONEXOES
    for link in area["connections"]:
      # CRIANDO OS LINKS
      links[count_links] = { "source": area["id"], "target": link }
      print("🚀 ~ count_links:", count_links)
      print("🚀 ~ link:", link)
      print("================")
      count_links = count_links + 1

  print("🚀 ~ links:", links)
  return { "nodes": nodes, "links": links }
  
  # const nodes = [
  #   { id: 'center', label: 'Centro 1' },
  #   { id: '2', label: 'Node 2' },
  #   { id: '3', label: 'Node 3' },
  #   { id: '4', label: 'Node 4' },
  # ];

  # const links = [
  #   { source: 'center', target: '2' },
  #   { source: 'center', target: '3' },
  #   { source: '2', target: '4' },
  #   { source: '3', target: '4' },
  # ];

  # let js = {
  #   'id': 'things_betwixt',
  #   'name': 'Things Betwixt',
  #   'description': 'Área tutorial inicial, lar das Guardiãs do Fogo.',
  #   'connections': ['majula'],
  #   'required_items': {}
  # }