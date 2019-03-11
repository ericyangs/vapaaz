
function CreateVapaaAction() {
    var vapaaActionJson = {
        "type": "vapaa_action",
        "message0": "Vapaa控制程式 %1",
        "args0": [
            {
                "type": "input_statement",
                "name": "ActionStatement"
            }
        ],
        "colour": 30,
        "tooltip": "",
        "helpUrl": ""
    };

    Blockly.Blocks['vapaa_action'] = {
        init: function () {
            this.jsonInit(vapaaActionJson);
            this.setTooltip(function () {
                return '請加入vapaa控制條件';
            });
        }
    };

    Blockly.Python['vapaa_action'] = function (block) {
        var importCode = "from GETPARAMS import _ai_type_data\n";
        importCode += "from GETPARAMS import _ai_org_data\n";
        importCode += "from GETPARAMS import _ai_real_data\n";
        importCode += "from GETPARAMS import _di_data\n";
        importCode += "from GETPARAMS import _do_data\n";
        importCode += "from GETPARAMS import _do_write_data\n";
        importCode += "from GETPARAMS import _ao_data\n";
        importCode += "from GETPARAMS import _ao_write_data\n";
        importCode += "import GETPARAMS\n\n";

        var funcName = Blockly.Python.variableDB_.getName("VapaaAction", Blockly.Procedures.NAME_TYPE);
        var branch = Blockly.Python.statementToCode(block, 'ActionStatement');
        if (Blockly.Python.STATEMENT_PREFIX) {
            branch = Blockly.Python.prefixLines(
                Blockly.Python.STATEMENT_PREFIX.replace(/%1/g,
                    '\'' + block.id + '\''), Blockly.Python.INDENT) + branch;
        }
        if (Blockly.Python.INFINITE_LOOP_TRAP) {
            branch = Blockly.Python.INFINITE_LOOP_TRAP.replace(/%1/g,
                '"' + block.id + '"') + branch;
        }
        if (!branch) {
            branch = Blockly.Python.PASS;
        }
        var code = importCode + 'def ' + funcName + '():\n' + branch;
        code = Blockly.Python.scrub_(block, code);
        return code;
    };

}

function CreateAITypeData() {
    var aiTypeDataJson = {
        "type": "ai_type_data",
        "message0": "讀取AI Type %1 ID %2 Port %3",
        "args0": [
            { "type": "input_dummy" },
            {
                "type": "field_number",
                "name": "id",
                "value": 1,
                "min": 1,
                "max": 16
            },
            {
                "type": "field_number",
                "name": "port",
                "value": 1,
                "min": 1,
                "max": 4
            }
        ],
        "inputsInline": false,
        "output": null,
        "colour": 30,
        "tooltip": "",
        "helpUrl": ""
    };

    Blockly.Blocks['ai_type_data'] = {
        init: function () {
            this.jsonInit(aiTypeDataJson);
            this.setTooltip(function () {
                return '讀取vapaa ai type';
            });
        }
    };

    Blockly.Python['ai_type_data'] = function (block) {
        var cardID = block.getFieldValue('id') || 0;
        var cardPort = block.getFieldValue('port') || 0;
        var code = "_ai_type_data[" + (cardID-1) + "][" + (cardPort-1) + "]";
        return [code, Blockly.Python.ORDER_MEMBER];
    };
}

function CreateAIData() {
    var aiDataJson = {
        "type": "ai_data",
        "message0": "讀取AI Data %1 ID %2 Port %3",
        "args0": [
            { "type": "input_dummy" },
            {
                "type": "field_number",
                "name": "id",
                "value": 1,
                "min": 1,
                "max": 16
            },
            {
                "type": "field_number",
                "name": "port",
                "value": 1,
                "min": 1,
                "max": 4
            }
        ],
        "inputsInline": false,
        "output": null,
        "colour": 30,
        "tooltip": "",
        "helpUrl": ""
    };

    Blockly.Blocks['ai_data'] = {
        init: function () {
            this.jsonInit(aiDataJson);
            this.setTooltip(function () {
                return '讀取vapaa ai data';
            });
        }
    };

    Blockly.Python['ai_data'] = function (block) {
        var cardID = block.getFieldValue('id') || 0;
        var cardPort = block.getFieldValue('port') || 0;
        var code = "_ai_org_data[" + (cardID-1) + "][" + (cardPort-1) + "]";
        return [code, Blockly.Python.ORDER_MEMBER];
    };
}

function CreateWriteDO() {
    var writeDOJson = {
        "type": "write_do",
        "message0": "寫入DO %1 ID %2 Port %3 value %4",
        "args0": [
            {"type": "input_dummy"},
            {
                "type": "field_number",
                "name": "id",
                "value": 1,
                "min": 1,
                "max": 16
            },
            {
                "type": "field_number",
                "name": "port",
                "value": 1,
                "min": 1,
                "max": 4
            },
            {
                "type": "input_value",
                "name": "doValue",
                "check": "Number"
            }
        ],
        "inputsInline": false,
        "previousStatement": null,
        "nextStatement": null,
        "colour": 30,
        "tooltip": "",
        "helpUrl": ""
    };

    Blockly.Blocks['write_do'] = {
        init: function () {
            this.jsonInit(writeDOJson);
            this.setTooltip(function () {
                return '寫入vapaa do卡';
            });
        }
    };

    Blockly.Python['write_do'] = function (block) {
        var cardID = block.getFieldValue('id') || 0;
        var cardPort = block.getFieldValue('port') || 0;
        var value = Blockly.Python.valueToCode(block, 'doValue',
            Blockly.Python.ORDER_NONE) || '\'\'';
        var code = "GETPARAMS._doactflag=1\n";
        code += "_do_write_data[" + (cardID-1) + "][" + (cardPort-1) + "]=int("+value+")\n";
        return code;
    };
}

CreateVapaaAction();
CreateAITypeData();
CreateAIData();
CreateWriteDO();