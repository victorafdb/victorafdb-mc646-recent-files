import sys
sys.path.insert(1,'/Users/victorf/Documents/unicamp/MC646/TDD/recent-files/src')

from recent_files import RecentFiles

# - Quando o programa está executando pela primeira vez, essa lista está vazia;
# - Quando um arquivo é aberto, ele é adicionado à lista de arquivos recentes;
# - Se um arquivo aberto já está na lista, este é levado ao topo da lista, sem conter itens duplicados na lista
# - Se a lista alcança seu limite (normalmente de 10 a 15 itens na lista), o item mais antigo é removido quando um novo item é adicionado.
# - A lista pode ser esvaziada a qualquer momento
# - A atualização da lista pode ser desabilitada/habilitada. Caso seja desabilitada, os arquivos já existentes ficarão na lista, mas não serão adicionados novos arquivos.

# Recent Files list is empty on init
def test_recent_files_initialization():
    recent_files = RecentFiles(10)
    assert recent_files.capacity == 10
    assert recent_files.load == 0

# Opening files

# Flushing Recent Files

# Blocking

# Unblocking