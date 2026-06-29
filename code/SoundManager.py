import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        self.sounds = {}
        self.music = None

    def load_sound(self, name, path):
        try:
            self.sounds[name] = pygame.mixer.Sound(path)
            print(f"✓ Som carregado: {name}")
        except Exception as e:
            print(f"Erro ao carregar som {name}: {e}")

    def play(self, name, volume=0.8):
        if name in self.sounds:
            self.sounds[name].set_volume(volume)
            self.sounds[name].play()
        else:
            print(f"Som não encontrado: {name}")

    def stop_sound(self, name):
        """Para um som específico (se estiver tocando)."""
        if name in self.sounds:
            self.sounds[name].stop()
            print(f"⏹ Som parado: {name}")

    def play_music(self, path, volume=0.5, loop=-1):
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loop)
            self.music = path
            print(f"♪ Música tocando: {path}")
        except Exception as e:
            print(f"Erro ao tocar música {path}: {e}")

    def stop_music(self):
        pygame.mixer.music.stop()
        print("⏹ Música parada")

    def set_music_volume(self, volume):
        pygame.mixer.music.set_volume(volume)