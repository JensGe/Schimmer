from kivy.app import App

import android


class AndroidApp(App):
    def build(self):
        android.vibrate(10)


AndroidApp().run()
