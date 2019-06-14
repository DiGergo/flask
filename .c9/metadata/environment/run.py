{"filter":false,"title":"run.py","tooltip":"/run.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":12,"column":0},"end":{"row":16,"column":74},"action":"remove","lines":["def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)"],"id":25},{"start":{"row":12,"column":0},"end":{"row":17,"column":74},"action":"insert","lines":["@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)"]}],[{"start":{"row":17,"column":74},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":26},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]},{"start":{"row":18,"column":4},"end":{"row":19,"column":0},"action":"insert","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["@"],"id":27},{"start":{"row":19,"column":1},"end":{"row":19,"column":2},"action":"insert","lines":["a"]},{"start":{"row":19,"column":2},"end":{"row":19,"column":3},"action":"insert","lines":["p"]},{"start":{"row":19,"column":3},"end":{"row":19,"column":4},"action":"insert","lines":["p"]},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["."]}],[{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["r"],"id":28},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["o"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["u"]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["t"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":12},"action":"insert","lines":["()"],"id":29}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["@"],"id":30}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"remove","lines":["@"],"id":31}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":[":"],"id":32}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"remove","lines":[":"],"id":33}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":13},"action":"insert","lines":["''"],"id":34}],[{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["/"],"id":35},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["a"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["b"]},{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"insert","lines":["o"]},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["u"]},{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["/"],"id":36},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["<"]}],[{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["m"],"id":37},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["e"]},{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["m"]},{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"insert","lines":["b"]},{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":["e"]},{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["r"]}],[{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"insert","lines":["_"],"id":38},{"start":{"row":19,"column":27},"end":{"row":19,"column":28},"action":"insert","lines":["n"]},{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"insert","lines":["a"]},{"start":{"row":19,"column":29},"end":{"row":19,"column":30},"action":"insert","lines":["m"]},{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":31},"end":{"row":19,"column":32},"action":"insert","lines":[">"],"id":39}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":40}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"insert","lines":["d"],"id":41},{"start":{"row":21,"column":1},"end":{"row":21,"column":2},"action":"insert","lines":["e"]},{"start":{"row":21,"column":2},"end":{"row":21,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":21,"column":3},"end":{"row":21,"column":4},"action":"insert","lines":[" "],"id":42},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["a"]},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["b"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["o"]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["u"]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["_"],"id":43},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["m"]},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["e"]},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["m"]},{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["b"]},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["e"]},{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":["r"]}],[{"start":{"row":21,"column":16},"end":{"row":21,"column":18},"action":"insert","lines":["()"],"id":44}],[{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["m"],"id":45},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["e"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["m"]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["b"]},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["e"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["r"]},{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["_"]}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["n"],"id":46},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["a"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["m"]},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":[":"],"id":47}],[{"start":{"row":21,"column":30},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":48},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["m"],"id":49},{"start":{"row":22,"column":5},"end":{"row":22,"column":6},"action":"insert","lines":["e"]},{"start":{"row":22,"column":6},"end":{"row":22,"column":7},"action":"insert","lines":["m"]},{"start":{"row":22,"column":7},"end":{"row":22,"column":8},"action":"insert","lines":["b"]},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["e"]},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["r"]}],[{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["="],"id":50}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":13},"action":"insert","lines":["[]"],"id":51}],[{"start":{"row":22,"column":13},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":52},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]},{"start":{"row":23,"column":4},"end":{"row":24,"column":0},"action":"insert","lines":["",""]},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":4},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":53},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]},{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"insert","lines":["w"]},{"start":{"row":24,"column":5},"end":{"row":24,"column":6},"action":"insert","lines":["i"]},{"start":{"row":24,"column":6},"end":{"row":24,"column":7},"action":"insert","lines":["t"]},{"start":{"row":24,"column":7},"end":{"row":24,"column":8},"action":"insert","lines":["h"]}],[{"start":{"row":24,"column":8},"end":{"row":24,"column":10},"action":"insert","lines":["()"],"id":54}],[{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["o"],"id":55},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["p"]},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["e"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["n"]}],[{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"remove","lines":["n"],"id":56},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"remove","lines":["e"]},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"remove","lines":["p"]},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"remove","lines":["o"]},{"start":{"row":24,"column":8},"end":{"row":24,"column":10},"action":"remove","lines":["()"]}],[{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"insert","lines":[" "],"id":57},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["o"]},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["p"]},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["e"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["n"]}],[{"start":{"row":24,"column":9},"end":{"row":24,"column":13},"action":"remove","lines":["open"],"id":58},{"start":{"row":24,"column":9},"end":{"row":24,"column":15},"action":"insert","lines":["open()"]}],[{"start":{"row":24,"column":14},"end":{"row":24,"column":16},"action":"insert","lines":["\"\""],"id":59}],[{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["d"],"id":60},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["a"]},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"insert","lines":["t"]},{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"insert","lines":["a"]},{"start":{"row":24,"column":19},"end":{"row":24,"column":20},"action":"insert","lines":["/"]},{"start":{"row":24,"column":20},"end":{"row":24,"column":21},"action":"insert","lines":["c"]}],[{"start":{"row":24,"column":21},"end":{"row":24,"column":22},"action":"insert","lines":["o"],"id":61},{"start":{"row":24,"column":22},"end":{"row":24,"column":23},"action":"insert","lines":["m"]},{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"insert","lines":["p"]},{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"insert","lines":["a"]},{"start":{"row":24,"column":25},"end":{"row":24,"column":26},"action":"insert","lines":["n"]},{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"insert","lines":["y"]}],[{"start":{"row":24,"column":27},"end":{"row":24,"column":28},"action":"insert","lines":["."],"id":62},{"start":{"row":24,"column":28},"end":{"row":24,"column":29},"action":"insert","lines":["j"]},{"start":{"row":24,"column":29},"end":{"row":24,"column":30},"action":"insert","lines":["o"]}],[{"start":{"row":24,"column":29},"end":{"row":24,"column":30},"action":"remove","lines":["o"],"id":63}],[{"start":{"row":24,"column":29},"end":{"row":24,"column":30},"action":"insert","lines":["s"],"id":64},{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["i"]}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"remove","lines":["i"],"id":65}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["o"],"id":66},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":["n"]}],[{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"insert","lines":[","],"id":67}],[{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"insert","lines":[" "],"id":68}],[{"start":{"row":24,"column":35},"end":{"row":24,"column":37},"action":"insert","lines":["\"\""],"id":69}],[{"start":{"row":24,"column":36},"end":{"row":24,"column":37},"action":"insert","lines":["r"],"id":70}],[{"start":{"row":24,"column":39},"end":{"row":24,"column":40},"action":"insert","lines":[" "],"id":71},{"start":{"row":24,"column":40},"end":{"row":24,"column":41},"action":"insert","lines":["a"]},{"start":{"row":24,"column":41},"end":{"row":24,"column":42},"action":"insert","lines":["s"]}],[{"start":{"row":24,"column":42},"end":{"row":24,"column":43},"action":"insert","lines":[" "],"id":72},{"start":{"row":24,"column":43},"end":{"row":24,"column":44},"action":"insert","lines":["j"]},{"start":{"row":24,"column":44},"end":{"row":24,"column":45},"action":"insert","lines":["s"]},{"start":{"row":24,"column":45},"end":{"row":24,"column":46},"action":"insert","lines":["o"]},{"start":{"row":24,"column":46},"end":{"row":24,"column":47},"action":"insert","lines":["n"]}],[{"start":{"row":24,"column":43},"end":{"row":24,"column":47},"action":"remove","lines":["json"],"id":73},{"start":{"row":24,"column":43},"end":{"row":24,"column":52},"action":"insert","lines":["json_data"]}],[{"start":{"row":24,"column":52},"end":{"row":24,"column":53},"action":"insert","lines":[":"],"id":74}],[{"start":{"row":24,"column":53},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":75},{"start":{"row":25,"column":0},"end":{"row":25,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["d"],"id":76},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["a"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["t"]},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["a"]}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":[" "],"id":77},{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":[" "],"id":78},{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["j"]},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["s"]},{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["o"]},{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"insert","lines":["n"]}],[{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"insert","lines":["."],"id":79},{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"insert","lines":["l"]},{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"insert","lines":["o"]},{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"insert","lines":["a"]},{"start":{"row":25,"column":23},"end":{"row":25,"column":24},"action":"insert","lines":["d"]}],[{"start":{"row":25,"column":24},"end":{"row":25,"column":26},"action":"insert","lines":["()"],"id":80}],[{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"insert","lines":["j"],"id":81},{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"insert","lines":["s"]},{"start":{"row":25,"column":27},"end":{"row":25,"column":28},"action":"insert","lines":["o"]},{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"insert","lines":["n"]},{"start":{"row":25,"column":29},"end":{"row":25,"column":30},"action":"insert","lines":["_"]},{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"insert","lines":["d"]}],[{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"insert","lines":["a"],"id":82},{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"insert","lines":["t"]},{"start":{"row":25,"column":33},"end":{"row":25,"column":34},"action":"insert","lines":["a"]}],[{"start":{"row":25,"column":35},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":83},{"start":{"row":26,"column":0},"end":{"row":26,"column":8},"action":"insert","lines":["        "]},{"start":{"row":26,"column":8},"end":{"row":26,"column":9},"action":"insert","lines":["f"]},{"start":{"row":26,"column":9},"end":{"row":26,"column":10},"action":"insert","lines":["o"]},{"start":{"row":26,"column":10},"end":{"row":26,"column":11},"action":"insert","lines":["r"]}],[{"start":{"row":26,"column":11},"end":{"row":26,"column":12},"action":"insert","lines":[" "],"id":84},{"start":{"row":26,"column":12},"end":{"row":26,"column":13},"action":"insert","lines":["o"]},{"start":{"row":26,"column":13},"end":{"row":26,"column":14},"action":"insert","lines":["b"]},{"start":{"row":26,"column":14},"end":{"row":26,"column":15},"action":"insert","lines":["j"]}],[{"start":{"row":26,"column":15},"end":{"row":26,"column":16},"action":"insert","lines":[" "],"id":85},{"start":{"row":26,"column":16},"end":{"row":26,"column":17},"action":"insert","lines":["i"]},{"start":{"row":26,"column":17},"end":{"row":26,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":26,"column":18},"end":{"row":26,"column":19},"action":"insert","lines":[" "],"id":86},{"start":{"row":26,"column":19},"end":{"row":26,"column":20},"action":"insert","lines":["d"]},{"start":{"row":26,"column":20},"end":{"row":26,"column":21},"action":"insert","lines":["a"]},{"start":{"row":26,"column":21},"end":{"row":26,"column":22},"action":"insert","lines":["t"]},{"start":{"row":26,"column":22},"end":{"row":26,"column":23},"action":"insert","lines":["a"]}],[{"start":{"row":26,"column":23},"end":{"row":26,"column":24},"action":"insert","lines":[":"],"id":87}],[{"start":{"row":26,"column":24},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":88},{"start":{"row":27,"column":0},"end":{"row":27,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":["i"],"id":89},{"start":{"row":27,"column":13},"end":{"row":27,"column":14},"action":"insert","lines":["f"]}],[{"start":{"row":27,"column":14},"end":{"row":27,"column":15},"action":"insert","lines":[" "],"id":90},{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"insert","lines":["o"]},{"start":{"row":27,"column":16},"end":{"row":27,"column":17},"action":"insert","lines":["b"]},{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"insert","lines":["j"]}],[{"start":{"row":27,"column":18},"end":{"row":27,"column":20},"action":"insert","lines":["[]"],"id":91}],[{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"insert","lines":["u"],"id":92},{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"insert","lines":["r"]},{"start":{"row":27,"column":21},"end":{"row":27,"column":22},"action":"insert","lines":["l"]}],[{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"insert","lines":["\""],"id":93}],[{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"insert","lines":["\""],"id":94}],[{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"insert","lines":[" "],"id":95},{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"insert","lines":["="]},{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"insert","lines":["="]}],[{"start":{"row":27,"column":28},"end":{"row":27,"column":29},"action":"insert","lines":[" "],"id":96},{"start":{"row":27,"column":29},"end":{"row":27,"column":30},"action":"insert","lines":["m"]},{"start":{"row":27,"column":30},"end":{"row":27,"column":31},"action":"insert","lines":["e"]},{"start":{"row":27,"column":31},"end":{"row":27,"column":32},"action":"insert","lines":["m"]},{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"insert","lines":["b"]},{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":27,"column":29},"end":{"row":27,"column":34},"action":"remove","lines":["membe"],"id":97},{"start":{"row":27,"column":29},"end":{"row":27,"column":40},"action":"insert","lines":["member_name"]}],[{"start":{"row":27,"column":40},"end":{"row":27,"column":41},"action":"insert","lines":[":"],"id":98}],[{"start":{"row":27,"column":41},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":99},{"start":{"row":28,"column":0},"end":{"row":28,"column":16},"action":"insert","lines":["                "]},{"start":{"row":28,"column":16},"end":{"row":28,"column":17},"action":"insert","lines":["m"]},{"start":{"row":28,"column":17},"end":{"row":28,"column":18},"action":"insert","lines":["e"]},{"start":{"row":28,"column":18},"end":{"row":28,"column":19},"action":"insert","lines":["m"]},{"start":{"row":28,"column":19},"end":{"row":28,"column":20},"action":"insert","lines":["b"]},{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"insert","lines":["e"]},{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"insert","lines":["r"]}],[{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"insert","lines":[" "],"id":100},{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"insert","lines":["="]}],[{"start":{"row":28,"column":24},"end":{"row":28,"column":25},"action":"insert","lines":[" "],"id":101},{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"insert","lines":["o"]},{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"insert","lines":["b"]},{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"insert","lines":["j"]}],[{"start":{"row":28,"column":25},"end":{"row":28,"column":28},"action":"remove","lines":["obj"],"id":102},{"start":{"row":28,"column":25},"end":{"row":28,"column":31},"action":"insert","lines":["object"]}],[{"start":{"row":28,"column":30},"end":{"row":28,"column":31},"action":"remove","lines":["t"],"id":103},{"start":{"row":28,"column":29},"end":{"row":28,"column":30},"action":"remove","lines":["c"]},{"start":{"row":28,"column":28},"end":{"row":28,"column":29},"action":"remove","lines":["e"]}],[{"start":{"row":28,"column":28},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":104},{"start":{"row":29,"column":0},"end":{"row":29,"column":16},"action":"insert","lines":["                "]},{"start":{"row":29,"column":16},"end":{"row":30,"column":0},"action":"insert","lines":["",""]},{"start":{"row":30,"column":0},"end":{"row":30,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"insert","lines":["r"],"id":105},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"insert","lines":["e"]},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"insert","lines":["t"]},{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"insert","lines":["u"]},{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"insert","lines":["r"]},{"start":{"row":30,"column":9},"end":{"row":30,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":30,"column":10},"end":{"row":30,"column":11},"action":"insert","lines":[" "],"id":106},{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"insert","lines":["r"]},{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"insert","lines":["e"]},{"start":{"row":30,"column":13},"end":{"row":30,"column":14},"action":"insert","lines":["n"]},{"start":{"row":30,"column":14},"end":{"row":30,"column":15},"action":"insert","lines":["d"]},{"start":{"row":30,"column":15},"end":{"row":30,"column":16},"action":"insert","lines":["e"]},{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":30,"column":17},"end":{"row":30,"column":29},"action":"remove","lines":["            "],"id":107},{"start":{"row":30,"column":17},"end":{"row":31,"column":0},"action":"insert","lines":["",""]},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"remove","lines":["    "],"id":108},{"start":{"row":30,"column":17},"end":{"row":31,"column":0},"action":"remove","lines":["",""]},{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"remove","lines":["t"]}],[{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"insert","lines":["r"],"id":109}],[{"start":{"row":30,"column":11},"end":{"row":30,"column":17},"action":"remove","lines":["render"],"id":110},{"start":{"row":30,"column":11},"end":{"row":30,"column":26},"action":"insert","lines":["render_template"]}],[{"start":{"row":30,"column":26},"end":{"row":30,"column":28},"action":"insert","lines":["()"],"id":111}],[{"start":{"row":30,"column":27},"end":{"row":30,"column":29},"action":"insert","lines":["\"\""],"id":112}],[{"start":{"row":30,"column":28},"end":{"row":30,"column":29},"action":"insert","lines":["m"],"id":113},{"start":{"row":30,"column":29},"end":{"row":30,"column":30},"action":"insert","lines":["e"]},{"start":{"row":30,"column":30},"end":{"row":30,"column":31},"action":"insert","lines":["m"]},{"start":{"row":30,"column":31},"end":{"row":30,"column":32},"action":"insert","lines":["b"]},{"start":{"row":30,"column":32},"end":{"row":30,"column":33},"action":"insert","lines":["e"]},{"start":{"row":30,"column":33},"end":{"row":30,"column":34},"action":"insert","lines":["r"]},{"start":{"row":30,"column":34},"end":{"row":30,"column":35},"action":"insert","lines":["."]}],[{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"insert","lines":["h"],"id":114},{"start":{"row":30,"column":36},"end":{"row":30,"column":37},"action":"insert","lines":["t"]},{"start":{"row":30,"column":37},"end":{"row":30,"column":38},"action":"insert","lines":["m"]},{"start":{"row":30,"column":38},"end":{"row":30,"column":39},"action":"insert","lines":["l"]}],[{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"insert","lines":[" "],"id":115}],[{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"insert","lines":[","],"id":116}],[{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"insert","lines":[" "],"id":117},{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"insert","lines":[" "]}],[{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"remove","lines":[" "],"id":118}],[{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"insert","lines":["m"],"id":119},{"start":{"row":30,"column":43},"end":{"row":30,"column":44},"action":"insert","lines":["e"]},{"start":{"row":30,"column":44},"end":{"row":30,"column":45},"action":"insert","lines":["m"]},{"start":{"row":30,"column":45},"end":{"row":30,"column":46},"action":"insert","lines":["b"]},{"start":{"row":30,"column":46},"end":{"row":30,"column":47},"action":"insert","lines":["e"]},{"start":{"row":30,"column":47},"end":{"row":30,"column":48},"action":"insert","lines":["r"]}],[{"start":{"row":30,"column":48},"end":{"row":30,"column":49},"action":"insert","lines":[" "],"id":120},{"start":{"row":30,"column":49},"end":{"row":30,"column":50},"action":"insert","lines":["="]}],[{"start":{"row":30,"column":49},"end":{"row":30,"column":50},"action":"remove","lines":["="],"id":121},{"start":{"row":30,"column":48},"end":{"row":30,"column":49},"action":"remove","lines":[" "]}],[{"start":{"row":30,"column":48},"end":{"row":30,"column":49},"action":"insert","lines":["="],"id":122}],[{"start":{"row":30,"column":49},"end":{"row":30,"column":50},"action":"insert","lines":[" "],"id":123}],[{"start":{"row":30,"column":49},"end":{"row":30,"column":50},"action":"remove","lines":[" "],"id":124}],[{"start":{"row":30,"column":49},"end":{"row":30,"column":50},"action":"insert","lines":["m"],"id":125},{"start":{"row":30,"column":50},"end":{"row":30,"column":51},"action":"insert","lines":["e"]},{"start":{"row":30,"column":51},"end":{"row":30,"column":52},"action":"insert","lines":["m"]},{"start":{"row":30,"column":52},"end":{"row":30,"column":53},"action":"insert","lines":["b"]},{"start":{"row":30,"column":53},"end":{"row":30,"column":54},"action":"insert","lines":["e"]},{"start":{"row":30,"column":54},"end":{"row":30,"column":55},"action":"insert","lines":["r"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":21,"column":30},"end":{"row":21,"column":30},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1560511127859,"hash":"24b7c692a79c5f8a00afd39fe7e853599fa75402"}