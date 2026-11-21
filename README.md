from kivy.app import App
from kivy.utils import platform

if platform == "android":
    from jnius import autoclass
    from android.runnable import run_on_ui_thread

    WebView = autoclass("android.webkit.WebView")
    WebViewClient = autoclass("android.webkit.WebViewClient")
    activity = autoclass("org.kivy.android.PythonActivity").mActivity


class GreenperpApp(App):

    def build(self):
        if platform == "android":
            self.open_webview()
            return None

        from kivy.uix.button import Button

        button = Button(text="Open Greenperp")
        button.bind(
            on_press=lambda x: __import__("webbrowser").open(
                "https://greenperp2.pythonanywhere.com/"
            )
        )
        return button

    @run_on_ui_thread
    def open_webview(self):
        webview = WebView(activity)
        webview.setWebViewClient(WebViewClient())
        webview.getSettings().setJavaScriptEnabled(True)
        webview.loadUrl(
            "https://greenperp2.pythonanywhere.com/"
        )
        activity.setContentView(webview)


if __name__ == "__main__":
    GreenperpApp().run()
