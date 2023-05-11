# Dzień 72 - Czy plik istnieje?
import os

filename = "plik.txt"
if os.path.exists(filename):
    print(f"Plik {filename} istnieje")
else:
    print(f"Plik {filename} nie istnieje")

# Jak można kopiować pliki?
import shutil

source = "plik.txt"
destination = "kopia_pliku.txt"

shutil.copy(source, destination)
print(f"Skopiowano {source} do {destination}")

# Jak przenieść plik?
import shutil

source = "plik_do_przeniesienia.txt"
destination = "przeniesiony_plik.txt"

shutil.move(source, destination)
print(f"Przeniesiono {source} do {destination}")

# Jak stworzyć folder?

import os

folder_name = "nowy_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Utworzono folder {folder_name}")
else:
    print(f"Folder {folder_name} już istnieje")

# Jak usunąć plik?
import os

filename = "do_usuniecia.txt"
if os.path.exists(filename):
    os.remove(filename)
    print(f"Usunięto plik {filename}")
else:
    print(f"Plik {filename} nie istnieje")

# Jak wyszukać pliki?
import glob

file_pattern = "*.txt"
files = glob.glob(file_pattern)

print("Znalezione pliki:")
for file in files:
    print(file)

# Jak rozbić nazwę pliku na nazwę i rozszerzenie?
import os

filename = "przykladowy_plik.txt"
file_basename, file_extension = os.path.splitext(filename)

print(f"Nazwa pliku bez rozszerzenia: {file_basename}")
print(f"Rozszerzenie pliku: {file_extension}")

# Zadanie
# 1.Utwórz folder źródłowy source oraz kilka plików tekstowych z różnymi rozszerzeniami, takimi jak .txt, .csv i .md.
import os

filename = "plik.txt"
if os.path.exists(filename):
    print(f"Plik {filename} istnieje")
else:
    print(f"Plik {filename} nie istnieje")

import os

folder_name = "source"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Utworzono folder {folder_name}")
else:
    print(f"Folder {folder_name} już istnieje")

folder_name = "plik.txt"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Utworzono folder {folder_name}")
else:
    print(f"Folder {folder_name} już istnieje")

folder_name = "plik.csv"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Utworzono folder {folder_name}")
else:
    print(f"Folder {folder_name} już istnieje")


folder_name = "plik.md"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Utworzono folder {folder_name}")
else:
    print(f"Folder {folder_name} już istnieje")

# 2. Napisz program, który wyszuka wszystkie pliki tekstowe w folderze źródłowym?
import glob

file_pattern = "*.txt"
files = glob.glob(file_pattern)

print("Znalezione pliki:")
for file in files:
    print(file)

# b.Dla każdego pliku utworzy folder docelowy (jeśli jeszcze nie istnieje) na podstawie rozszerzenia pliku.
import os

filename = "plik.txt"
file_basename, file_extension = os.path.splitext(filename)

print(f"Nazwa pliku bez rozszerzenia: {file_basename}")
print(f"Rozszerzenie pliku: {file_extension}")

import os

filename = "plik.csv"
file_basename, file_extension = os.path.splitext(filename)

print(f"Nazwa pliku bez rozszerzenia: {file_basename}")
print(f"Rozszerzenie pliku: {file_extension}")

import os

filename = "plik.md"
file_basename, file_extension = os.path.splitext(filename)

print(f"Nazwa pliku bez rozszerzenia: {file_basename}")
print(f"Rozszerzenie pliku: {file_extension}")

# c. Przeniesie plik do odpowiedniego folderu docelowego
import shutil

source = "plik_do_przeniesienia.txt"
destination = "przeniesiony_plik.txt"

shutil.move(source, destination)
print(f"Przeniesiono {source} do {destination}")

import shutil

source = "plik_do_przeniesienia.csv"
destination = "przeniesiony_plik.csv"

shutil.move(source, destination)
print(f"Przeniesiono {source} do {destination}")

import shutil

source = "plik_do_przeniesienia.md"
destination = "przeniesiony_plik.md"

shutil.move(source, destination)
print(f"Przeniesiono {source} do {destination}")
