using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class StickScript : MonoBehaviour {

	private Vector3 startPosition;
	private bool mouseDown = false;


	void Start () {
		this.startPosition = this.gameObject.transform.position;
	}


	void Update () {
		if (Input.GetMouseButtonDown (0)) {
			mouseDown = true;
			//this.gameObject.transform.GetComponents

		} else if (mouseDown) {
			this.gameObject.GetComponent<Rigidbody> ().AddForce (new Vector3 (0, 0, 400));
			this.mouseDown = false;
		}
	}

}