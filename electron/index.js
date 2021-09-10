const { app, BrowserWindow } = require('electron');

function createWindow () {
	const win = new BrowserWindow({
	  width: 1000,
	  height: 700,
	  minWidth: 1000,
	  minHeight: 700,
	  icon: './icon.png'
	})
	win.loadFile('./src/index.html')
}

app.whenReady().then(() => {
	createWindow()

	app.on('activate', function () {
	  if (BrowserWindow.getAllWindows().length === 0) createWindow()
	})
  })

app.on('window-all-closed', function () {
	if (process.platform !== 'darwin') app.quit()
})
