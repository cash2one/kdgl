/*
Navicat MySQL Data Transfer

Source Server         : wemanage
Source Server Version : 50624
Source Host           : localhost:3306
Source Database       : kdgl

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2017-03-30 16:35:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) DEFAULT NULL,
  `username` varchar(30) CHARACTER SET utf8 DEFAULT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 DEFAULT NULL,
  `last_name` varchar(30) CHARACTER SET utf8 DEFAULT NULL,
  `email` varchar(75) CHARACTER SET utf8 DEFAULT NULL,
  `is_staff` tinyint(1) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `date_joined` datetime DEFAULT NULL,
  `number` varchar(20) CHARACTER SET utf8 NOT NULL COMMENT '快递员编号',
  `phone` varchar(20) CHARACTER SET utf8 NOT NULL,
  `performance` varchar(20) CHARACTER SET utf8 NOT NULL DEFAULT '0' COMMENT '绩效',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$12000$AdRMxgn7EJqZ$TkAVrZOX0ALtHNKNs5HEUyhd+1DSrtGfc/83FSi47fY=', '2017-03-24 10:28:26', '1', 'chenggong', '', '', 'liulian5675@qq.com', '1', '1', '2017-03-23 16:34:43', '003', '18565458784', '0.00');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$12000$tHWjHjO21JQZ$Ih1RbKbOlU5/MLz/VwryWhTu0DeV8HyeqWXC8GAiPaA=', '2017-03-29 17:25:38', '0', 'kdgl', '', '', '', '0', '1', '2017-03-23 16:50:52', '002', '15265458565', '2.0');
INSERT INTO `auth_user` VALUES ('7', 'pbkdf2_sha256$12000$E0vRwm05Uv3J$HxlasYrljXgyDUXbNK7ockVE4+toOhRn1fS7ObFr1wg=', null, null, 'xhw', null, null, null, null, null, null, '006', '185485658754', '0.00');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2017-03-23 16:50:52', '1', '4', '2', 'kdgl', '1', '');

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'log entry', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'permission', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'group', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('4', 'user', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'content type', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'session', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('7zhx7i3vk6w16xqd459uf5l3xzjl7i1z', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-07 10:28:50');
INSERT INTO `django_session` VALUES ('8zsr41hnqpb48vm3ksbliyf2qhbr44n7', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-07 16:32:45');
INSERT INTO `django_session` VALUES ('96b3g7naffofqturi3ofyohqne1krpus', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-07 17:02:26');
INSERT INTO `django_session` VALUES ('akkz4kk6m4mlds7i6dg1zf871ox2kr9x', 'Y2E3OWJkOTRjNTA1MTMyYzQwMWJmODAzNWQ3MmUxYTM1MzAzMTZhNjp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfaWQiOjIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2017-04-07 16:35:58');
INSERT INTO `django_session` VALUES ('ds5s5rjxg3bgpq6axe8cp9zodvyilepw', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-07 15:38:47');
INSERT INTO `django_session` VALUES ('e60snnlcjnp3sx5o3gruqyaeohtncscl', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-11 18:32:06');
INSERT INTO `django_session` VALUES ('ejgm7uyfvrtn7kp45wjmnao1tdnkcwv1', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-07 15:29:47');
INSERT INTO `django_session` VALUES ('iaikoxuunauorfwmtxpb78v0d36qefkg', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-12 17:25:38');
INSERT INTO `django_session` VALUES ('mrn7l6w4uwm9sy2llruuuzuxtzqkp8c1', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-12 17:18:24');
INSERT INTO `django_session` VALUES ('q43wbztx0tzrcqn445d90ngj1oeb7ija', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-07 17:26:54');
INSERT INTO `django_session` VALUES ('q8t4r9dl5utym4z55h53ze4ok7skrfez', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-07 18:57:19');
INSERT INTO `django_session` VALUES ('rfok4noor6lvs6oqskx4h8mxmiy1z6kn', 'Y2E3OWJkOTRjNTA1MTMyYzQwMWJmODAzNWQ3MmUxYTM1MzAzMTZhNjp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfaWQiOjIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2017-04-07 16:58:04');
INSERT INTO `django_session` VALUES ('skt1j72hwbf85lmk8rnqr5ulwz36xanb', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-12 15:33:09');
INSERT INTO `django_session` VALUES ('tum0domnvw8syv0mrq1funhm18ujexns', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-11 18:10:32');
INSERT INTO `django_session` VALUES ('ue3vwc08l9d0oesh66y282cg82o8hcoc', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-11 18:00:37');
INSERT INTO `django_session` VALUES ('uo4pliruffhgd2kiyvsy1ou45h89fp9i', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-07 16:34:26');
INSERT INTO `django_session` VALUES ('w7g2hfsksvsplr65nzjck98isvz43cf9', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-07 17:25:09');
INSERT INTO `django_session` VALUES ('wvbefromqgq0gg8ctcfa7m617vd3z5bz', 'Y2E3OWJkOTRjNTA1MTMyYzQwMWJmODAzNWQ3MmUxYTM1MzAzMTZhNjp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfaWQiOjIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2017-04-10 10:00:21');
INSERT INTO `django_session` VALUES ('x3ixfzf1ysvzboybhatwxekpnidx1hh5', 'YjQzY2EwNTQ3MWQ4ZjlkZGI5MWZlMDE2ZjgzZDZmYmJlNjViZWQzMDp7InVzZXJuYW1lIjoia2RnbCIsInBhc3N3b3JkIjoia2RnbCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2017-04-07 16:36:30');

-- ----------------------------
-- Table structure for `express_info`
-- ----------------------------
DROP TABLE IF EXISTS `express_info`;
CREATE TABLE `express_info` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `type` varchar(1) NOT NULL COMMENT '快递类型1-发快递 2-收快递',
  `express_classification` varchar(3) NOT NULL DEFAULT '0' COMMENT '快递种类0小包，1-中包，2-大包，3-特大包',
  `express_money` double(20,0) DEFAULT '0' COMMENT '快递费用',
  `express_user_id` varchar(20) DEFAULT NULL COMMENT '快递员编号',
  `express_number` varchar(50) NOT NULL COMMENT '快递单号',
  `sender_name` varchar(200) DEFAULT NULL,
  `sender_phone` varchar(20) DEFAULT NULL,
  `sender_address` varchar(200) DEFAULT NULL,
  `reciver_name` varchar(200) DEFAULT NULL,
  `reciver_phone` varchar(20) DEFAULT NULL,
  `reciver_address` varchar(200) DEFAULT NULL,
  `shelf_number` varchar(20) DEFAULT NULL COMMENT '货架编号',
  `express_status` varchar(2) NOT NULL COMMENT '物流状态0-待发货，1-在路上，2-待查收，3-已查收',
  `created_at` varchar(20) NOT NULL COMMENT '快递日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of express_info
-- ----------------------------
INSERT INTO `express_info` VALUES ('14', '1', '1', '20', '002', '201525252512', '天琪', '18565458784', '山东省滨州市邹平县西王集团', '王玉婷', '18565485785', '湖北省武汉市永宁区宽窄巷子201号', '3', '2', '2017-03-13 00:00:00');
INSERT INTO `express_info` VALUES ('15', '2', '3', '30', '002', '2015425451254', '占磊', '15845876585', '北京朝阳区神州大道102号', '杜浩', '18554585652', '北京东城区泺源大街1332号', '5', '1', '2017-03-15 00:00:00');
INSERT INTO `express_info` VALUES ('19', '2', '2', '30', '002', '2017052512545215', '成先生', '18564587584', '山东省济南市高新区120号', '夏女士', '18545685236', '北京市昌平区回龙观镇3024号', '6', '0', '2017-03-07 00:00:00');
