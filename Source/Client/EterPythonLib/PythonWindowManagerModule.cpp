/// 1. Ignore if it already exists
// Search
PyObject* wndButtonSetUpVisual(PyObject* poSelf, PyObject* poArgs)

// Add above
PyObject* wndImageResetFrame(PyObject* poSelf, PyObject* poArgs)
{
	UI::CWindow* pWindow;
	if (!PyTuple_GetWindow(poArgs, 0, &pWindow))
		return Py_BuildException();

	((UI::CAniImageBox*)pWindow)->ResetFrame();

	return Py_BuildNone();
}

/// 2. Ignore if it already exists
// Search
		{ "AppendImage", wndImageAppendImage, METH_VARARGS },

// Add below
		{ "ResetFrame", wndImageResetFrame, METH_VARARGS },
