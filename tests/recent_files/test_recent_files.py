import sys
import pytest
sys.path.insert(
    1, '/Users/victorf/Documents/unicamp/MC646/TDD/recent-files/src')

from recent_files import RecentFiles, File


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


def test_recent_files_initialization_forbidden_capacity():
    with pytest.raises(ValueError):
        recent_files = RecentFiles(-1)

# Opening files


def test_recent_files_register_new_file_success():
    recent_files = RecentFiles(10)
    opened_file = File("file1.txt", "This is file one")
    recent_files.register_file(opened_file)
    assert recent_files.load == 1
    assert recent_files.searchForFileByPath(
        opened_file.path).content == opened_file.content


def test_recent_files_register_multiple_files_success():
    recent_files = RecentFiles(10)
    opened_file = File("file1.txt", "This is file 1")
    opened_file2 = File("file2.txt", "This is file 2")
    recent_files.register_file(opened_file)
    recent_files.register_file(opened_file2)
    assert recent_files.load == 2
    assert recent_files.searchForFileByPath(
        opened_file.path).content == opened_file.content
    assert recent_files.searchForFileByPath(
        opened_file2.path).content == opened_file2.content


def test_recent_files_register_known_file_success():
    recent_files = RecentFiles(10)
    opened_file = File("file1.txt", "This is file 1")
    opened_file2 = File("file2.txt", "This is file 2")
    opened_file3 = File("file1.txt", "This is file 1")
    recent_files.register_file(opened_file)
    recent_files.register_file(opened_file2)
    recent_files.print_list()
    recent_files.register_file(opened_file3)
    assert recent_files.load == 2
    assert recent_files.searchForFileByPath(
        opened_file.path).content == opened_file.content
    assert recent_files.searchForFileByPath(
        opened_file2.path).content == opened_file2.content
    assert recent_files.searchForFileByPath(
        opened_file3.path).content == opened_file3.content

    # Make sure the known_file is the first element in the list
    assert recent_files.head.path == opened_file3.path


def test_recent_files_register_over_limit():
    recent_files = RecentFiles(3)
    opened_file = File("file1.txt", "This is file 1")
    opened_file2 = File("file2.txt", "This is file 2")
    opened_file3 = File("file3.txt", "This is file 3")
    opened_file4 = File("file4.txt", "This is file 4")
    recent_files.register_file(opened_file)
    recent_files.register_file(opened_file2)
    recent_files.register_file(opened_file3)
    recent_files.register_file(opened_file4)
    assert recent_files.load == 3

    # Make sure the oldest file gets removed
    assert recent_files.searchForFileByPath(
        opened_file.path) is None
    assert recent_files.searchForFileByPath(
        opened_file2.path).content == opened_file2.content
    assert recent_files.searchForFileByPath(
        opened_file3.path).content == opened_file3.content
    assert recent_files.searchForFileByPath(
        opened_file4.path).content == opened_file4.content

# Flushing Recent Files

# Blocking

# Unblocking
