import sublime, sublime_plugin, re

class FormatLuaBeforeSave(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        if re.search("lua$",view.file_name()):
            view.run_command("format_lua")
