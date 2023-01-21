from pytube import Youtube
import pytube
import os

def main():
  link = input('Digite o link do vídeo do YouTube para fazer a conversão: ')

  if os.name == 'nt':
    path = os.getcwd() + '\\'
  else:
    path = os.getcwd() + '/'
  
  name = pytube.extract.video_id(link)
  Youtube(link).streams.filter(only_audio=True).first().download(filename=name)
  location = path + name + '.mp4'
  mp3_name = path + name + '.mp3' 

  if os.name == 'nt':  
    os.system(f'ren {location} {mp3_name}')
  else:
    os.system(f'mv {location} {mp3_name}')

if __name__ == '__main__':
  main()