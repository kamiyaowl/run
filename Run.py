import sublime, sublime_plugin, threading, subprocess, json

class RunCommand(sublime_plugin.WindowCommand):
	def run(self):
		active_view = self.window.active_view()
		path = active_view.file_name()
		#open setting file
		f = open("setting.json","r")
		setting = json.load(f)
		f.close();
		#select command
		command = ""
		args = []
		for k in setting.keys():
			if path.find(k) != -1:
				command = setting[k]["path"] + " " + path
		if command == "":
			print "No match setting.json commands."
			return
		print command
		sublime.status_message(command)
		def work():
			proc = subprocess.Popen(command, shell=True, bufsize=4096, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
			for line in proc.stdout:
				print line,

		thread = threading.Thread(target = work)
		thread.start()