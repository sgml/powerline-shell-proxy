import subprocess

def add_svn_segment():
	try:
		is_svn = subprocess.Popen(['svn', 'status'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		is_svn_output = is_svn.communicate()[1].strip()
		if len(is_svn_output) != 0:
			return

		#"svn status | grep -c "^[ACDIMRX\\!\\~]"
		p1 = subprocess.Popen(['svn', 'status'], stdout=subprocess.PIPE,
			stderr=subprocess.PIPE)
		p2 = subprocess.Popen(['grep', '-c', '^[ACDIMR\\!\\~]'],
			stdin=p1.stdout, stdout=subprocess.PIPE)
		output = p2.communicate()[0].strip()
		if len(output) > 0 and int(output) > 0:
			changes = output.strip()
			powerline.append(' %s ' % changes, Color.SVN_CHANGES_FG, Color.SVN_CHANGES_BG)
	except OSError:
		pass
	except subprocess.CalledProcessError:
		pass

powerline.register( add_svn_segment )
