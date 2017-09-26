using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveTextureScript : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}

    private float count = 0;
	// Update is called once per frame
	void Update ()
	{
	    count += Time.deltaTime;
        Renderer renderer = GetComponent<Renderer>();
	    renderer.material.mainTextureOffset = new Vector2(count, count);

	    if (count > 10)
	    {
	        count = 0;
	    }
	}
}
