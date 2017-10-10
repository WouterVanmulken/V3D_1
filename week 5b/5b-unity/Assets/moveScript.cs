using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class moveScript : MonoBehaviour {
	public Rigidbody rb;
	float speed = 1;
	// Use this for initialization
	void Start () {
		this.rb = GetComponent<Rigidbody> ();
	}
	
	// Update is called once per frame
	void Update () {
		//float moveHorizontal = Input.GetAxis ("Horizontal");
		//float moveVertical = Input.GetAxis ("Vertical");



		if (Input.GetKey ("w")) {
			Vector3 movement = new Vector3 (0, 0.0f, -1);
			rb.velocity = movement * speed;
		}

		if (Input.GetKey ("a")) {
			Vector3 movement = new Vector3 (0, 0.0f, 1);
			rb.velocity = movement * speed;
		}
		if (Input.GetKey ("s")) {
			Vector3 movement = new Vector3 (-1, 0.0f, 0);
			rb.velocity = movement * speed;
		}
		if (Input.GetKey ("d")) {
			Vector3 movement = new Vector3 (1, 0.0f, 0);
			rb.velocity = movement * speed;
		}
	}
}
