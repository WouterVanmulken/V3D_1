﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RotateScript : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		this.gameObject.transform.Rotate (new Vector3 (-.1f,0,0));
	}
}
