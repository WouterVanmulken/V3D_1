using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveScript : MonoBehaviour {
	public float speed;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
	    if (Input.GetKey(KeyCode.LeftArrow))
	    {
	        Vector3 position = this.transform.position;
			position.x-=speed;
	        this.transform.position = position;
	    }
	    if (Input.GetKey(KeyCode.RightArrow))
	    {
	        Vector3 position = this.transform.position;
			position.x+=speed;
	        this.transform.position = position;
	    }
	    if (Input.GetKey(KeyCode.UpArrow))
	    {
	        Vector3 position = this.transform.position;
			position.z+=speed;
	        this.transform.position = position;
	    }
	    if (Input.GetKey(KeyCode.DownArrow))
	    {
	        Vector3 position = this.transform.position;
			position.z-=speed;
	        this.transform.position = position;
	    }
    }
}
