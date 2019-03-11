
var blocklyArea = document.getElementById('blocklyArea');
var blocklyDiv = document.getElementById('blocklyDiv');
var workspace = Blockly.inject(blocklyDiv, {
    toolbox: document.getElementById('toolbox'),
    zoom: { controls: true, wheel: true },
});

function onresize() {
    var element = blocklyArea;
    var x = 0;
    var y = 0;
    do {
        x += element.offsetLeft;
        y += element.offsetTop;
        element = element.offsetParent;
    } while (element);
    // Position blocklyDiv over blocklyArea.
    blocklyDiv.style.left = x + 'px';
    blocklyDiv.style.top = y + 'px';
    blocklyDiv.style.width = blocklyArea.offsetWidth + 'px';
    blocklyDiv.style.height = blocklyArea.offsetHeight + 'px';
    Blockly.svgResize(workspace);
}

function DownloadStringAsFile(filename,data){
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(data));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

function ExportPythonCode() {
    var code = Blockly.Python.workspaceToCode(workspace);
    DownloadStringAsFile("vapaaAction.py",code);
}

workspace.registerButtonCallback("exportPythonCode", ExportPythonCode);

function UpdateCode(event) {
    //var xml = Blockly.Xml.workspaceToDom(workspace);
    //console.log(xml);
    var code = Blockly.Python.workspaceToCode(workspace);
    document.getElementById('genCode').value = code;
}
workspace.addChangeListener(UpdateCode);

window.addEventListener("load", function () {
    onresize();
    //set default blocks in workspace
    Blockly.Xml.domToWorkspace(document.getElementById('defaultBlock'), workspace);
});

window.addEventListener('resize', onresize);