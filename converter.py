from pytube import YouTube
import pytube
import os

def main():
  link = input('Digite o link do vídeo do YouTube para fazer a conversão: ')

  print(os.name)

  if os.name == 'nt':
    path = os.getcwd() + '\\'
  else:
    path = os.getcwd() + '/'
  
  name = pytube.extract.video_id(link)
  YouTube(link).streams.filter(only_audio=True).first().download(filename=name)
  print(f'path = {path}')
  print(f'name = {name}')
  location = path + name + '.mp4'
  mp3_name = path + name + '.mp3'
  print(f'location = {location}')
  print(f'mp3 name = {mp3_name}')

  if os.name == 'nt':  
    os.system('ren {0}{1}'.format(location, mp3_name))
  else:
    os.system('mv {0}{1}'.format(location, mp3_name))

if __name__ == '__main__':
  main()