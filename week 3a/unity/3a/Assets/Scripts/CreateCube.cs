using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CreateCube : MonoBehaviour {

	// Use this for initialization
	void Start () {
	    Mesh mesh = GetComponent<MeshFilter>().mesh;
        //Vector3[] vertices = mesh.vertices;

        Vector3[] vertices = new Vector3[]
        {
            new Vector3(0,0,0),
            new Vector3(0,1,0),
            new Vector3(0,1,1),
            new Vector3(0,0,1)
        };

	    mesh.vertices = vertices;
	    mesh.RecalculateBounds();
        
    }
	
	// Update is called once per frame
	void Update () {
		
	}
}
