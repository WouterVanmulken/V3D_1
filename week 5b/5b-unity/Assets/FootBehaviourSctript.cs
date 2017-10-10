using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FootBehaviourSctript : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		Joint joint = GetComponent<Joint>();
	    Joint joint2 = joint.connectedBody.gameObject.GetComponent<Joint>();


	    joint.transform.rotation = new Quaternion(joint2.transform.rotation.eulerAngles.x,0,0,0);// = .Rotate(joint2.transform.rotation.eulerAngles.x,0,0);;
	}
}
