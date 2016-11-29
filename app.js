var nRows = 8;
var nColumns = 8;

function row(x) {
    return parseInt(x / nColumns);
}

function col(x) {
    return x % nColumns;
}

function neighbour(x, y) {
    return row(x) == row(y) + 1 || row(x) == row(y) - 1 || col(x) == col(y) + 1 || col(x) == col(y) - 1;
}

var width = 1000, height = 600;
var g = {
    nodes: [],
    edges: []
};

for (var i = 0; i < numOfVertex; i++) {
    g.nodes.push({
        id: 'n' + geos[i][0],
        label: 'node ' + geos[i][0],
        x: geos[i][1] * 100,
        y: geos[i][2] * 100,
        size: 1,
        color: '#666'
    });
}


for (var i = 0; i < numOfEdge; i++) {
    var x = edges[i][0], y = edges[i][1];
    var type;
    if (neighbour(x, y)) {
        type = 'curve';
    } else {
        type = 'curve';
    }
    
    g.edges.push({
        id: 'e' + i,
        // label: 'edge ' + edges[i][0] + ' : ' + edges[i][1],
        source: 'n' + edges[i][0],
        target: 'n' + edges[i][1],
        color: '#ccc',
        size: 2,
        type: 'line'
    })
}

var s = new sigma({
    graph: g,
    // container: 'graph_container',
    renderer: {
        container: document.getElementById('graph_container'),
        type: 'canvas'
    },
    settings: {
        // edgeLabelSize: 'proportional',
        // doubleClickEnabled: true,
        // minEdgeSize: 0.5,
        // maxEdgeSize: 4,
        // enableEdgeHovering: true,
        // edgeHoverColor: 'edge',
        // defaultEdgeHoverColor: '#000',
        // edgeHoverSizeRatio: 1,
        // edgeHoverExtremities: true,
        
        enableEdgeHovering: true,
        // defaultEdgeHoverColor: '#fff',
        edgeHoverSizeRatio: 2

    }
});

// Click or Hover on a node
// s.bind('overNode clickNode', function(e) {
//   console.log(e.type, e.data.node.label, e.data.captor);
//   console.log(s.graph.edges[0])
// });

// Initialize the dragNodes plugin:
var dragListener = sigma.plugins.dragNodes(s, s.renderers[0]);

dragListener.bind('startdrag', function(event) {
  // console.log(event);
});
dragListener.bind('drag', function(event) {
  // console.log(event);
});
dragListener.bind('drop', function(event) {
  // console.log(event);
});
dragListener.bind('dragend', function(event) {
  // console.log(event);
});

